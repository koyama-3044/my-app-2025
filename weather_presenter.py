# weather_presenter.py
import webbrowser
import os
from typing import List
from .weather_data import WeatherData

class WeatherPresenter:
    """気象データをHTML形式で整形し、ブラウザで表示するクラス"""
    def display_weather_data(self, weather_list: List[WeatherData], location: str):
        """
        気象データのリストをHTML形式で生成し、一時ファイルとして保存後、ブラウザで開く。

        Args:
            weather_list (List[WeatherData]): 表示する気象データのリスト
            location (str): 表示する場所の名前
        """
        html_content = self._generate_html(weather_list, location)
        
        # 一時ファイルにHTMLを書き込む
        file_path = "weather_report.html"
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"気象レポートが '{file_path}' に保存されました。")
            webbrowser.open(f"file://{os.path.realpath(file_path)}")
        except IOError as e:
            print(f"ファイルの書き込みまたはブラウザの起動に失敗しました: {e}")

    def _generate_html(self, weather_list: List[WeatherData], location: str) -> str:
        """
        気象データのリストからHTMLコンテンツを生成する。
        """
        html = f"""
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{location}の3時間ごとの天気予報</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background-color: #f4f7f6; color: #333; }}
                h1 {{ color: #0056b3; text-align: center; margin-bottom: 30px; }}
                .weather-container {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }}
                .weather-card {{
                    background-color: #ffffff;
                    border: 1px solid #e0e0e0;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    padding: 20px;
                    width: 280px;
                    box-sizing: border-box;
                    transition: transform 0.2s;
                }}
                .weather-card:hover {{
                    transform: translateY(-5px);
                }}
                .weather-card h2 {{
                    color: #28a745;
                    margin-top: 0;
                    font-size: 1.3em;
                    border-bottom: 1px solid #eee;
                    padding-bottom: 10px;
                    margin-bottom: 15px;
                }}
                .weather-card p {{
                    margin: 8px 0;
                    font-size: 1.05em;
                }}
                .weather-card p strong {{
                    color: #555;
                }}
            </style>
        </head>
        <body>
            <h1>{location}の3時間ごとの天気予報</h1>
            <div class="weather-container">
        """

        for data in weather_list:
            html += f"""
                <div class="weather-card">
                    <h2>{data.time}</h2>
                    <p><strong>天気:</strong> {data.weather}</p>
                    <p><strong>気温:</strong> {data.temperature:.1f}°C</p>
                    <p><strong>湿度:</strong> {data.humidity}%</p>
                    <p><strong>風速:</strong> {data.wind_speed:.1f} m/s</p>
                </div>
            """
        
        html += """
            </div>
        </body>
        </html>
        """
        return html