import pytest
import json

@pytest.fixture
def load_json():
    with open("./data.json") as in_json, open("./data_out.json") as out_json:
        yield [json.load(in_json), json.load(out_json)]
        in_json.close()
        out_json.close()

# Compare total number of records
def test_customer_count(load_json):
    in_json, out_json = load_json
    in_rec_count = len(in_json)
    out_rec_count_customers = len(out_json['customers'])
    out_rec_count_orders = len(out_json['orders'])
    assert (in_rec_count == out_rec_count_customers == out_rec_count_orders), "No. of records in output JSON are not matching!, expected:{} customer_records:{} order_records:{}".format(in_rec_count, out_rec_count_customers, out_rec_count_orders)

# Compare number of orders for first vendor
def test_orders_per_vendor(load_json):
    in_json, out_json = load_json
    in_num_orders = len(in_json[0]['order'])
    out_num_orders = len(out_json['orders'][0]['order'])
    assert (in_num_orders == out_num_orders), "No. of orders for first vendor are not matching!, expected:{} found:{}".format(in_num_orders, out_num_orders)

# Validate revenue per order
def test_revenue_per_order(load_json):
    out_json = load_json[1]
    for order in out_json['orders']:
        for item in order['order']:
            assert item['revenue'] == item['quantity'] * item['price'], "Revenue per order is not valid, expected: {}, found: {}".format(item['quantity'] * item['price'], item['revenue'])

