#!/bin/sh
start=$(python timestamp.py)

echo "Running All Tests"
echo ""

echo "-- Day 01 --"
python3 day01.py
echo "-- Day 02 --"
python3 day02.py
echo "-- Day 03 --"
python3 day03.py
echo "-- Day 04 --"
python3 day04.py
echo "-- Day 05 --"
python3 day05.py
echo "-- Day 06 --"
python3 day06.py
echo "-- Day 07 --"
python3 day07.py
echo "-- Day 08 --"
python3 day08.py
echo "-- Day 09 --"
python3 day09.py
echo "-- Day 10 --"
python3 day10.py
echo "-- Day 11 --"
python3 day11.py
echo "-- Day 12 --"
python3 day12.py
echo "-- Day 13 --"
python3 day13.py
echo "-- Day 14 --"
python3 day14.py


end=$(python timestamp.py) 
runtime=$(python -c "print(${end} - ${start})")
echo ""
echo "Total runtime: $runtime"