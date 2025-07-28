# weather_fetcher.py
import requests

class WeatherFetcher:
    """外部の気象情報APIからデータを取得するクラス"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/forecast"

    def fetch_weather_data(self, location: str) -> dict:
        """
        指定された場所の3時間ごとの気象データをAPIから取得する。

        Args:
            location (str): 気象情報を取得する場所 (例: "Funabashi,JP")

        Returns:
            dict: APIから取得した生データ（JSON形式）

        Raises:
            requests.exceptions.RequestException: APIリクエスト中にエラーが発生した場合
            ValueError: APIからの応答が不正な場合
        """
        params = {
            "q": location,
            "appid": self.api_key,
            "units": "metric",  # 摂氏で取得
            "lang": "ja"        # 日本語で取得
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"APIリクエストエラー: {e}")
            raise
        except ValueError as e:
            print(f"APIからの応答が不正です: {e}")
            raise