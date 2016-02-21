create DATABASE IF NOT EXISTS stp;

USE stp;

DROP TABLE IF EXISTS stocks;
DROP TABLE IF EXISTS insider;


--CREATE TABLE IF NOT EXISTS stocks (
--    quote_id varchar(100) NOT NULL,
--    symbol varchar(20),  
--    last_price float,
--    low_price float,
--    high_price float,
--    changeytd float,
--    msdate varchar(40),
--    market_cap varchar(40),
--    price_open float,
--    price_change float,
--    stock_date DATE DEFAULT NULL,
--    volume integer,
--    change_percent float,
--    PRIMARY KEY(quote_id)
--);


CREATE TABLE IF NOT EXISTS stocks (
    quote_id varchar(100) NOT NULL,
    symbol varchar(20),  
    last_price varchar(50),
    low_price varchar(50),
    high_price varchar(50),
    changeytd varchar(50),
    msdate varchar(40),
    market_cap varchar(40),
    price_open varchar(50),
    price_change varchar(50),
    stock_date varchar(50),
    volume varchar(50),
    change_percent varchar(50),
    PRIMARY KEY(quote_id)
);

