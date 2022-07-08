import json

# Construct a new order structure with item and revenue fields
#
#  - Adds item field with the value of the order's key in input json
#  - Adds revenue field as quantity * price value

def consolidate_order(order):
    cons_orders = []
    for item in order.keys():
        cons_order = {
                "item" : item,
                "quantity" : order[item]['quantity'],
                "price" : order[item]['price'],
                "revenue" : order[item]['quantity'] * order[item]['price']
                }
        cons_orders.append(cons_order)
    return cons_orders

# Transforms  JSON input file
#
# Input file : ./data.json
# Output file: ./data_out.json
def transform_json():
    in_json = open('./data.json')
    in_data = json.load(in_json)
    customers = []
    orders = []

    # Iterate each record in input JSON
    #   Build customer and order array objects with required fields and sequence
    for r in in_data:
        cust = {
                "id" : r['customer']['id'],
                "name" : r['customer']['name'],
                "address" : r['customer']['address']
                }
        customers.append(cust)
        cons_order = consolidate_order(r['order'])

        ord = {
                "id" : r['id'],
                "vendor" : r['vendor'],
                "date" : r['date'],
                "customer" : r['customer']['id'],
                "order" : cons_order
                }
        orders.append(ord)

    # Build a structure with customer and order arrays to final JSON
    out_json_obj = {
            "customers": customers,
            "orders": orders
            }

    with open("./data_out.json", "w") as out_json:
        json.dump(out_json_obj, out_json, indent = 4)

    in_json.close()
    out_json.close()

# main function
def main():
    print("Transforming JSON..")
    transform_json()
    print("JSON transformation is complete!")

if __name__ == "__main__":
    main()

################################### End of the file ########################################################
