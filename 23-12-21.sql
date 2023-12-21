SELECT t.name, g.name from tracks t
LEFT JOIN genres g on t. GenreId = g.GenreId 


















1. How many hours of songs exist in the application?

SELECT SUM(Milliseconds) / (1000 * 60 * 60) AS Total_Hours
FROM tracks;

SELECT sum(cast (Milliseconds as REAL))/3600000 as total_hours from tracks;


2. Get top 5 countries with most customers in descenging order

SELECT Country, COUNT(*) AS CustomerCount
FROM customers
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 5;


3. which customer email domain is the most popular? give counts of top 3

SELECT substr(Email, instr(Email, '@' ) +1) as EmailDomain, count(*) as totalEmail FROM customers GROUP by EmailDomain order by totalEmail DESC LIMIT 3


4. Which artist has most songs in the application

SELECT ar.name as artisName, Count(*) as totalArtist from tracks t LEFT JOIN albums a on t.AlbumId= a.AlbumId
LEFT JOIN artists ar on a.ArtistId=ar.ArtistId GROUP by ar.name order by totalArtist DESC


5. How many songs are in the playlist on average?

SELECT avg(SongsinPlay)  from (SELECT PlaylistId, count(1) as SongsinPlay FROM playlist_track GROUP by PlaylistId);

6.Which country generates most revenue give top 5

SELECT BillingCountry as Country, sum(total)as Total_sales FROM invoices GROUP by BillingCountry ORDER by sum(total) DESC LIMIT 5;

7.Which customer generated most revenue, give top 5

SELECT c.FirstName ||" "|| c.LastName as customer,  sum(i.total) as Total_revenue from invoices i LEFT JOIN customers c on i.CustomerId = c.CustomerId group by i.CustomerId ORDER by sum(i.total)DESC LIMIT 5;

8 with each and every artist count how many songs they made in each genre

-- 8.with each and every artist count how many songs they made in each genre
SELECT Composer, COUNT(*) FROM (

SELECT 
    Composer,
    b.Name,
    COUNT(TrackId) AS 'Song made'
FROM
    tracks a
        LEFT JOIN
    genres b ON a.GenreId = b.GenreId
WHERE
    Composer IS NOT NULL
GROUP BY 1 , 2
ORDER BY 3 DESC)
group by 1
HAVING COUNT(*) > 1
ORDER BY 2 DESC;


Select b.Name FROM tracks a LEFT JOIN  genres b ON a.GenreId = b.GenreId where a.Composer = "Steve Harris" group by 1;

