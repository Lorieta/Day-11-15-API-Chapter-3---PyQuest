from flask import Flask, jsonify


app = Flask(__name__)

aws_services = [
    {"id": 1, "service": "Lambda"},
    {"id": 2, "service": "Simple Storage Service(S3)"},
    {"id": 3, "service": "Elastic Compute Cloud(EC2)"},
    {"id": 4, "service": "Relational Database Service(RDS)"},
    {"id": 5, "service": "Elastic Container Service(ECS)"},
]


# base url
@app.route("/", methods=["GET"])
def hello():
    return jsonify("Hello")


# /aws_services/get_all
@app.route("/aws_services/get_all", methods=["GET"])
def get_all():
    return jsonify(aws_services)


# /aws_services/<int:service_id>
@app.route("/aws_services/<int:service_id>", methods=["GET"])
def get_service(service_id):
    try:
        service = aws_services[service_id]
        return jsonify(service)
    except:
        return "Service not found"


# /aws_services/add_service
@app.route("/aws_services/add_service", methods=["GET", "POST"])
def add_service():
    newService = {"id": 6, "service": "Identity and Access Management(IAM)"}
    aws_services.append(newService)
    return jsonify(aws_services)


# /aws_services/delete_service/<int:service_id>
@app.route("/aws_services/delete_service/<int:service_id>", methods=["GET", "DELETE"])
def delete_service(service_id):

    for service in aws_services:
        if service["id"] == service_id:
            aws_services.remove(service)
        return jsonify(aws_services)
    return jsonify({"error": "Service not found"})


# /aws_services/update_service/<int:service_id>
@app.route("/aws_services/update_service/<int:service_id>", methods=["GET", "PATCH"])
def update_service(service_id):
    data = {"id": 7, "service": "Amazon RDS Proxy"}
    for service in aws_services:
        if service["id"] == service_id:
            service.update(data)
            return jsonify(aws_services)
    return jsonify({"error": "Service not found"})


if __name__ == "__main__":
    app.run(debug=True)
