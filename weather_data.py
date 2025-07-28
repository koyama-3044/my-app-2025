# weather_data.py
from dataclasses import dataclass

@dataclass
class WeatherData:
    """気象データの構造を定義するデータクラス"""
    time: str
    weather: str
    temperature: float
    humidity: int
    wind_speed: float

    def __str__(self):
        """表示用の文字列を返す"""
        return (f"時刻: {self.time}, 天気: {self.weather}, 気温: {self.temperature:.1f}°C, "
                f"湿度: {self.humidity}%, 風速: {self.wind_speed:.1f}m/s")