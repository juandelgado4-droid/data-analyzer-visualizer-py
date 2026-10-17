"""
Statistical Report Generator
Generates clean terminal output and exported Markdown/HTML reports.
"""

from typing import Dict, Any
from .analyzer import DatasetAnalyzer


class ReportGenerator:
    def __init__(self, analyzer: DatasetAnalyzer):
        self.analyzer = analyzer

    def print_terminal_report(self) -> None:
        print("\n" + "=" * 64)
        print("      EXPLORATORY DATA ANALYSIS (EDA) STATISTICAL REPORT       ")
        print("=" * 64)

        total_rows = len(self.analyzer.rows)
        total_cols = len(self.analyzer.headers)
        numeric_cols = list(self.analyzer.numeric_columns.keys())

        print(f"[*] Total Records:  {total_rows}")
        print(f"[*] Total Columns:  {total_cols}")
        print(f"[*] Numeric Fields: {len(numeric_cols)} {numeric_cols}\n")

        print("--- [ DESCRIPTIVE NUMERICAL PROFILING ] ---")
        for col in numeric_cols:
            stats = self.analyzer.compute_summary_stats(col)
            print(f"\n>> Column: [{col}]")
            print(f"   Count:   {stats['count']} | Mean: {stats['mean']} | StdDev: {stats['std_dev']}")
            print(f"   Min:     {stats['min']} | Median: {stats['median']} | Max: {stats['max']}")
            print(f"   IQR:     {stats['iqr']} | Detected Outliers: {stats['outliers_count']}")
            print("   Distribution Histogram:")
            print(self.analyzer.generate_ascii_histogram(col, bins_count=6))

        if len(numeric_cols) >= 2:
            print("\n--- [ PEARSON CORRELATION MATRIX ] ---")
            header_str = "              " + "".join(f"{c[:10]:>12}" for c in numeric_cols)
            print(header_str)
            for c1 in numeric_cols:
                row_str = f"{c1[:12]:<14}"
                for c2 in numeric_cols:
                    corr = self.analyzer.compute_pearson_correlation(c1, c2)
                    row_str += f"{corr:12.3f}"
                print(row_str)
        print("\n" + "=" * 64 + "\n")

    def export_markdown_report(self, output_path: str) -> None:
        numeric_cols = list(self.analyzer.numeric_columns.keys())
        lines = [
            "# 📊 Automated Exploratory Data Analysis Report\n",
            f"- **Total Rows Analyzed**: `{len(self.analyzer.rows)}`",
            f"- **Total Columns**: `{len(self.analyzer.headers)}`",
            f"- **Numerical Columns**: `{', '.join(numeric_cols)}`\n",
            "## 📈 Numerical Summary Statistics\n",
            "| Column | Count | Mean | Std Dev | Min | Median | Max | IQR | Outliers |",
            "|---|---|---|---|---|---|---|---|---|",
        ]

        for col in numeric_cols:
            s = self.analyzer.compute_summary_stats(col)
            lines.append(
                f"| `{col}` | {s['count']} | {s['mean']} | {s['std_dev']} | {s['min']} | {s['median']} | {s['max']} | {s['iqr']} | {s['outliers_count']} |"
            )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
