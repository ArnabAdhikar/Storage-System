from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    
    try:
        san_iops = int(data['san_iops'])
        standalone_iops = int(data['standalone_iops'])
        san_latency = float(data['san_latency'])
        standalone_latency = float(data['standalone_latency'])
        san_cost = float(data['san_cost'])
        standalone_cost = float(data['standalone_cost'])
    except (ValueError, KeyError) as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400

    # Print received values for debugging
    print(f"Received data: {data}")
    standalone_iops = int(data['standalone_iops'])

    san_latency = float(data['san_latency'])
    standalone_latency = float(data['standalone_latency'])

    san_cost = float(data['san_cost'])
    standalone_cost = float(data['standalone_cost'])

    result = {
        'IOPS': [san_iops, standalone_iops],
        'Latency': [san_latency, standalone_latency],
        'Cost': [san_cost, standalone_cost]
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
