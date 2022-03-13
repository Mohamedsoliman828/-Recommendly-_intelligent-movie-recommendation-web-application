import util
from flask import Flask,jsonify,request, render_template
app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    mov=request.form['title']
    print(mov)
    temp = util.get_recommendations(mov)
    #print(temp)
    rec = temp.tolist()
    resp_dic = {'rec': rec}
    print(resp_dic)
    resp = jsonify(resp_dic)
    print(resp)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp



if __name__ =='__main__':
    util.load_artifacts()
    app.run(port=5000,debug =True)

