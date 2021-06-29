import pytest



if __name__ == '__main__':
    pytest.main(["-s", "test_enterprise_Management.py","test_customer_Management.py","test_commodity_Management.py",
                 "test_content_Management.py","test_order_Management.py","test_marketing_Promotion.py","test_page_Layout.py",
                 "test_payment_Management.py","test_data_Analysis.py"
                 ])