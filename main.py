#!/usr/bin/env python3
"""
CLI entry point for Data Analyzer & Visualizer
"""

import sys
import argparse
from eda_toolkit.analyzer import DatasetAnalyzer
from eda_toolkit.reporter import ReportGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Automated Exploratory Data Analysis & Statistical Profiling CLI"
    )
    parser.add_argument(
        "--file", "-f",
        default="sample_data.csv",
        help="Path to CSV dataset to profile (defaults to sample_data.csv)",
    )
    parser.add_argument(
        "--export-md", "-m",
        help="Optional path to export a clean Markdown summary report",
    )

    args = parser.parse_args()

    try:
        analyzer = DatasetAnalyzer(args.file)
        reporter = ReportGenerator(analyzer)

        reporter.print_terminal_report()

        if args.export_md:
            reporter.export_markdown_report(args.export_md)
            print(f"[+] Exported Markdown report to: {args.export_md}")

    except FileNotFoundError:
        print(f"[-] Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error during analysis: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
