# weather_parser.py
from datetime import datetime
from typing import List
from .weather_data import WeatherData

class WeatherParser:
    """取得したJSONデータを整形し、WeatherDataオブジェクトに変換するクラス"""
    def parse_weather_data(self, raw_data: dict) -> List[WeatherData]:
        """
        APIから取得した生データをパースし、WeatherDataオブジェクトのリストに変換する。

        Args:
            raw_data (dict): APIから取得した生データ

        Returns:
            List[WeatherData]: 3時間ごとの気象データのリスト
        """
        parsed_data = []
        if "list" not in raw_data:
            print("エラー: 'list'キーがありません。API応答の形式が不正です。")
            return []

        for item in raw_data["list"]:
            try:
                # 3時間ごとのデータのみを抽出 (OpenWeatherMapのforecastはデフォルトで3時間ごと)
                dt_object = datetime.fromtimestamp(item["dt"])
                time = dt_object.strftime("%Y-%m-%d %H:%M")
                weather_description = item["weather"][0]["description"]
                temperature = item["main"]["temp"]
                humidity = item["main"]["humidity"]
                wind_speed = item["wind"]["speed"]

                parsed_data.append(
                    WeatherData(time, weather_description, temperature, humidity, wind_speed)
                )
            except KeyError as e:
                print(f"データのパース中にキーエラーが発生しました: {e}. 不正なデータ項目: {item}")
                continue
            except Exception as e:
                print(f"データのパース中に予期せぬエラーが発生しました: {e}. 項目: {item}")
                continue
        return parsed_data