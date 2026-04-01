from flask import Flask,request,jsonify, render_template

sk = Flask(__name__,template_folder="./")

@sk.route("/", methods=["GET"])
def sayhello():
   return render_template("index.html",name="Shin Khant")

@sk.route("/post", methods=["POST"])
def fromClients():
    data = request.get_json()
    age = data.get("age")
    name = data["name"]

    if age >= 18:
        return jsonify({
            "Message" : "You are luu gyi"
        })

    return jsonify({
        "Message" : "You are KID "
    })

    

if __name__ == "__main__":
    sk.run(host="0.0.0.0",port=4444,debug=True)

    



