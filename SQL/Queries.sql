--Most common openings for each rating range
SELECT opening_name, 
CASE WHEN black_rating<1600 and white_rating <1600 THEN "less than 1600" 
when black_rating>= 1600 and white_rating>=1600 and black_rating<2000 and white_rating<2000 then "Lies between 1600 and 2000"
Else "Above 2000"
END 
As rating_range , Count(*)

FROM `sixth-decoder-463706-n9.kaggle_chess_analytics.Main`

group by opening_name,rating_range
order by rating_range	

--Calculating white win rate
SELECT opening_name, SUM(CASE WHEN winner='white' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS white_win_rate

FROM `sixth-decoder-463706-n9.kaggle_chess_analytics.Main`

GROUP BY opening_name
ORDER BY white_win_rate DESC
limit 1000

