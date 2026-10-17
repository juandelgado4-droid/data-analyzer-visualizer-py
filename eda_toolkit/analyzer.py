"""
Dataset Statistical Profiler & Analyzer
Calculates descriptive statistics, quartile ranges, outlier detection, and correlation matrices.
Implemented without mandatory external dependencies using standard Python mathematics.
"""

import csv
import math
from typing import List, Dict, Any, Tuple, Optional


class DatasetAnalyzer:
    def __init__(self, filepath: Optional[str] = None):
        self.headers: List[str] = []
        self.rows: List[Dict[str, Any]] = []
        self.numeric_columns: Dict[str, List[float]] = {}
        if filepath:
            self.load_csv(filepath)

    def load_csv(self, filepath: str) -> None:
        with open(filepath, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.headers = reader.fieldnames or []
            self.rows = list(reader)

        self._profile_types()

    def _profile_types(self) -> None:
        self.numeric_columns = {}
        for col in self.headers:
            parsed_vals = []
            is_numeric = True
            for r in self.rows:
                raw = r[col].strip() if r[col] else ""
                if raw == "":
                    continue
                try:
                    parsed_vals.append(float(raw))
                except ValueError:
                    is_numeric = False
                    break
            if is_numeric and len(parsed_vals) > 0:
                self.numeric_columns[col] = parsed_vals

    def compute_summary_stats(self, col: str) -> Dict[str, float]:
        data = sorted(self.numeric_columns.get(col, []))
        n = len(data)
        if n == 0:
            return {}

        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / (n - 1) if n > 1 else 0.0
        std_dev = math.sqrt(variance)

        # Median & Quartiles
        median = data[n // 2] if n % 2 != 0 else (data[n // 2 - 1] + data[n // 2]) / 2.0
        q1 = data[int(n * 0.25)]
        q3 = data[int(n * 0.75)]
        iqr = q3 - q1

        # Outlier count via Tukey's fences
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        outliers = [x for x in data if x < lower_fence or x > upper_fence]

        return {
            "count": n,
            "min": data[0],
            "max": data[-1],
            "mean": round(mean, 3),
            "std_dev": round(std_dev, 3),
            "median": round(median, 3),
            "q1": round(q1, 3),
            "q3": round(q3, 3),
            "iqr": round(iqr, 3),
            "outliers_count": len(outliers),
        }

    def compute_pearson_correlation(self, col1: str, col2: str) -> float:
        d1 = self.numeric_columns.get(col1, [])
        d2 = self.numeric_columns.get(col2, [])
        n = min(len(d1), len(d2))
        if n < 2:
            return 0.0

        mean1 = sum(d1[:n]) / n
        mean2 = sum(d2[:n]) / n

        numerator = sum((d1[i] - mean1) * (d2[i] - mean2) for i in range(n))
        denom1 = math.sqrt(sum((d1[i] - mean1) ** 2 for i in range(n)))
        denom2 = math.sqrt(sum((d2[i] - mean2) ** 2 for i in range(n)))

        if denom1 * denom2 == 0:
            return 0.0

        return round(numerator / (denom1 * denom2), 3)

    def generate_ascii_histogram(self, col: str, bins_count: int = 8) -> str:
        data = self.numeric_columns.get(col, [])
        if not data:
            return ""

        min_val = min(data)
        max_val = max(data)
        if min_val == max_val:
            return f"[{min_val}]: {'#' * len(data)}"

        step = (max_val - min_val) / bins_count
        bins = [0] * bins_count

        for x in data:
            idx = int((x - min_val) / step)
            if idx >= bins_count:
                idx = bins_count - 1
            bins[idx] += 1

        max_bin = max(bins) if max(bins) > 0 else 1
        histogram_lines = []

        for i in range(bins_count):
            bin_start = min_val + i * step
            bin_end = bin_start + step
            bar_len = int((bins[i] / max_bin) * 28)
            bar = "█" * bar_len
            histogram_lines.append(f"  [{bin_start:6.1f} - {bin_end:6.1f}] | {bar} ({bins[i]})")

        return "\n".join(histogram_lines)
