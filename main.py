# main.py
from .config import API_KEY, LOCATION
from .weather_fetcher import WeatherFetcher
from .weather_parser import WeatherParser
from .weather_presenter import WeatherPresenter

class WeatherApp:
    """気象情報を取得し、表示するアプリケーションのメインクラス"""
    def __init__(self, api_key: str, location: str):
        self.weather_fetcher = WeatherFetcher(api_key)
        self.weather_parser = WeatherParser()
        self.weather_presenter = WeatherPresenter()
        self.location = location

    def run(self):
        """アプリケーションを実行し、気象情報を取得・表示する"""
        print(f"{self.location}の気象情報を取得中...")
        try:
            raw_data = self.weather_fetcher.fetch_weather_data(self.location)
            weather_list = self.weather_parser.parse_weather_data(raw_data)
            
            if weather_list:
                self.weather_presenter.display_weather_data(weather_list, self.location)
                print("気象情報の表示が完了しました。ブラウザをご確認ください。")
            else:
                print("気象データを取得できませんでした。")
        except Exception as e:
            print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    if API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        print("エラー: config.py に OpenWeatherMap APIキーを設定してください。")
        print("APIキーは https://openweathermap.org/api で無料で取得できます。")
    else:
        app = WeatherApp(api_key=API_KEY, location=LOCATION)
        app.run()