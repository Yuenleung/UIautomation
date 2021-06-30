import os

import pytest

if __name__ == '__main__':
    run_path = os.path.dirname(os.path.abspath(__file__))
    testcasepath = run_path + '\\testcase\\'
    testlist = ["test_enterprise_Management.py", "test_customer_Management.py", "test_commodity_Management.py",
                "test_content_Management.py", "test_order_Management.py", "test_marketing_Promotion.py",
                "test_page_Layout.py", "test_payment_Management.py", "test_data_Analysis.py", "test_system_Settings.py"]
    testlist = list(map(lambda x: testcasepath + x, testlist))
    testlist.append('-s')
    pytest.main(testlist)
