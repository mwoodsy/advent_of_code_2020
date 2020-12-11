#!/bin/sh
start=$(python timestamp.py)

echo "Running All Tests"
echo ""

echo "-- Day 01 --"
python day01.py
echo "-- Day 02 --"
python day02.py
echo "-- Day 03 --"
python day03.py
echo "-- Day 04 --"
python day04.py
echo "-- Day 05 --"
python day05.py
echo "-- Day 06 --"
python day06.py
echo "-- Day 07 --"
python day07.py
echo "-- Day 08 --"
python day08.py
echo "-- Day 09 --"
python day09.py
echo "-- Day 10 --"
python day10.py


end=$(python timestamp.py) 
runtime=$(python -c "print(${end} - ${start})")
echo ""
echo "Total runtime: $runtime"