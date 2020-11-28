#!/bin/bash
# test Travis CI
find . -name "*.pyc" -exec rm {} \;
coverage run -p --source=tests,helloworld -m unittest # this is where you add the
                                                      # folders you want to test
if [ "$?" = "0" ]; then
    coverage combine
    echo -e "\n\n================================================"
    echo "Test Coverage"
    coverage report
    echo -e "\nrun \"coverage html\" for full report"
    echo -e "\n"

    # pyflakes or its like should go here
fi

python -m doctest -v  tests/test_test.py
