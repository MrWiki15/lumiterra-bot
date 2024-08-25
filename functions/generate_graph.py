import matplotlib.pyplot as plt
import io

# Mapeo de las temporalidades
TEMPORALITY_MAP = {
    "Last 24h": "last_24h",
    "Last 7d": "last_7d",
    "Last 30d": "last_30d"
}

def generate_graph(data, chart_type, temp_key):
    plt.figure(figsize=(10, 5))
    
    # Convertir la temporalidad al formato correcto para acceder a los datos
    temp_key = TEMPORALITY_MAP.get(temp_key, temp_key)

    chart_data = None

    if chart_type == "Average price":
        chart_data = data['data']['collectionAnalytics']['mkpValueCharts']['average_price_chart'].get(temp_key)

    elif chart_type == "Floor price":
        chart_data = data['data']['collectionAnalytics']['mkpValueCharts']['floor_price_chart'].get(temp_key)

    elif chart_type == "MKP sale":
        chart_data = data['data']['collectionAnalytics']['mkpValueCharts']['mkp_sales_chart'].get(temp_key)

    elif chart_type == "MKP Volume":
        chart_data = data['data']['collectionAnalytics']['mkpValueCharts']['mkp_volume_chart'].get(temp_key)

    if chart_data is None:
        raise ValueError(f"No data available for {chart_type} with temporality {temp_key}")

    times = [entry['start'] for entry in chart_data]
    values = [entry['value'] for entry in chart_data]

    plt.plot(times, values, label=f'{chart_type} ({temp_key})')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(f'{chart_type} over {temp_key}')
    plt.legend()
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return buf