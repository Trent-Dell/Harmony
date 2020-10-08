CREATE TABLE GNS(
    GCS TEXT NOT NULL,
    combinedPT TEXT NOT NULL,
    combinedPC TEXT NOT NULL,
    PT TEXT NOT NULL,
    PC TEXT NOT NULL,
	FFD TEXT NOT NULL,
    PRIMARY KEY (PT)
    );

CREATE TABLE arev (
    DPN VARCHAR(5) NOT NULL,
--     DPN TEXT NOT NULL,
    Descrip TEXT NOT NULL,
    PC TEXT NOT NULL,
    PT TEXT NOT NULL,
    Phase TEXT NOT NULL,
    Create_Date DATE,
    GCS TEXT,
    CPC TEXT,
    CPT TEXT,
    UNIQUE (DPN)
    -- FOREIGN KEY (PT) REFERENCES GNS (PT)
);

CREATE TABLE xrev (
    DPN VARCHAR(5) NOT NULL, 
--     DPN TEXT NOT NULL,
    Descrip TEXT,
    PC TEXT,
    PT TEXT,
    Phase TEXT NOT NULL,
    UNIQUE (DPN),
    Create_Date DATE,
    GCS TEXT,
    CPC TEXT,
    CPT TEXT,
    -- FOREIGN KEY (PT) REFERENCES GNS (PT),
    UNIQUE (DPN)
);

copy <table_name>  from '/source_file.csv' delimiter ';' TXT HEADER ;

SELECT * FROM GNS;

-- Data cleanse
	-- remove all non x-rev from life cycle phase; keep 'X Revision'
	-- remove all nulls from PC & PT columns
	-- remove all non DPN (5 digit char limit)

-- 213482 DPNs in file before dropping non X-rev
DELETE FROM XREV WHERE Phase <> 'X Revision';
-- 213357 DPNs after cleaning phase

SELECT DPN,length(DPN) as "valid DPN" from xrev
	where length(DPN)<6;
-- 182747 returned

DELETE FROM XREV WHERE length(DPN) > 5;
-- deleted 30610; 182747 remaining

SELECT COUNT (PT) from XREV where (PT) is NULL;

SELECT * INTO Xclean FROM XREV
	WHERE (PHASE = 'X Revision') AND (length(DPN) < 6);

SELECT * FROM Xclean;

drop table gns cascade;

SELECT * FROM aREV LIMIT 100;

SELECT COUNT(PT) FROM GNS;

SELECT COUNT(PT) FROM xrev where "PT" is Null;
SELECT COUNT(dpn) FROM xrev;

SELECT COUNT(DPN) FROM arev;

-- clean arev, export as aclean
SELECT COUNT (DPN) FROM AREV;
	-- returned 1457511
SELECT COUNT (PT) from aREV where (PT) is NULL; -- 0 nulls for PT
SELECT COUNT (PHASE) FROM AREV WHERE "phase" = "A Revison";
	-- returned 1457511; the total count
SELECT DPN,length(DPN) as "valid DPN" from arev
	where length(DPN)<6;
-- 1393712 returned
SELECT * from "valid DPN";

DELETE FROM AREV WHERE Phase <> 'A Revision';
	-- 0 deleted, ALL were Arev
DELETE FROM AREV WHERE length(DPN) > 5;
-- deleted 63799; 1393712 remaining
SELECT * FROM AREV;

CREATE TABLE arevCleaned (
    -- DPN VARCHAR(5) NOT NULL, input file includes non DPN & non parts
    DPN TEXT NOT NULL,
    Descrip TEXT NOT NULL,
    PC TEXT NOT NULL,
    PT TEXT NOT NULL,
    Phase TEXT NOT NULL,
    UNIQUE (DPN),
    FOREIGN KEY (PT) REFERENCES GNS (PT)
);

SELECT * INTO aclean FROM aREV
	WHERE (PHASE = 'A Revision') AND (length(DPN) < 6);
select * from aclean;
-- join arev/xrev to GNS
	-- append attributes to arev/xrev
SELECT xr.dpn, xr.pc, xr.pt, gcs, combinedpt, combinedpc
INTO Xrev_newAttr FROM gns
LEFT JOIN xclean as xr ON (gns.pt = xr.pt);

SELECT * FROM Xrev_newAttr;
	-- 181127

SELECT ar.dpn, ar.pc, ar.pt, gcs, combinedpt, combinedpc
INTO Arev_newAttr FROM gns
LEFT JOIN aclean as ar ON (gns.pt = ar.pt);

SELECT * FROM Arev_newAttr;
	-- 1390244 