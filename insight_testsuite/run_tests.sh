#!/bin/bash

# Test 1 - Verify app handles 500 normal records
echo "test 1 in progress"
python3 ../src/insight.py  ./test_1/input/products.csv ./test_1/input/order_products_500.csv ./test_1/output/report_test.csv
if [ $(diff ./test_1/output/report_known_good.csv ./test_1/output/report_test.csv | wc -l) -gt 0 ]; then
  echo "Test 1 failed"
else
  echo "Test 1 successful"
fi

# Test 2 - Verify app handles bad data gracefully
echo "test 2 in progress"
python3 ../src/insight.py  ./test_2/input/products.csv ./test_2/input/order_products_100_bad.csv ./test_2/output/report_test.csv
if [ $(diff ./test_2/output/report_known_good.csv ./test_2/output/report_test.csv | wc -l) -gt 0 ]; then
  echo "Test 2 failed"
else
  echo "Test 2 successful"
fi

# Test 3 - Verify app handles missing inputs gracefully
echo "test 3 in progress"
if python3 ../src/insight.py  ./test_3/input/product_does_not_exist.csv ./test_3/input/order_does_not_exist.csv ./test_2/output/report.csv | grep "Products file does not exist" ; then
  echo "Test 3 successful"
else
  echo "Test 3 failed"
fi
