from elasticsearch import Elasticsearch

es=Elasticsearch("http://localhost:9200/",request_timeout=100)

es
document={
    "name":"Yash Kumar",
    "age": 20,
    "department": "Data Science",
    "occupation": "Data Engineer",
    "branch": "Pune",
    "sex":"Male"
}

es.index(index="emp",id=1,document=document)

query = {
    "query" :{
        "match":{
            "branch":"Pune"
        }
    }
}
response= es.search(index="emp",body=query)

print("Search Results: ",response)

response["hits"]["hits"]
