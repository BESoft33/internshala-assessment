# Test the endpoints at
`Invoice`
http://localhost:8000/api/invoices/

`Details`
http://localhost:8000/api/details/

Use this format to send body of post request to add invoice:
<pre>
{
"customer_name" : "Customer",
"invoice":[
    {
        "description": "Test",
        "unit_price":2,
        "quantity":6,
        "price":12
    }
]
}
</pre>
