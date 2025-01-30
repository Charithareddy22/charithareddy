{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOeVy1fV4T/Mvwtj6cF6sgh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Charithareddy22/charithareddy/blob/main/pharma.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.metrics import mean_squared_error\n",
        "\n",
        "# Load the dataset (make sure to replace the path with the actual path of your dataset)\n",
        "# Assuming dataset is in a CSV file format\n",
        "df = pd.read_csv('drug_data.csv')\n",
        "\n",
        "# Data Cleaning (check for missing values, data types, and basic cleaning)\n",
        "df.isnull().sum()  # Checking for missing values\n",
        "df.dropna(inplace=True)  # Drop rows with missing values (you can also fill them based on context)\n",
        "df.dtypes  # Check for data types\n",
        "\n",
        "# Assuming the columns in the dataset are: Product, Region, Trial_Period, Effectiveness, Side_Effects, Marketing_Spend\n",
        "# If needed, you can convert columns to appropriate data types (e.g., categorical variables to category type)\n",
        "\n",
        "df['Product'] = df['Product'].astype('category')\n",
        "df['Region'] = df['Region'].astype('category')\n",
        "df['Trial_Period'] = df['Trial_Period'].astype('category')\n",
        "\n",
        "# Now proceed to create the visualizations:\n",
        "\n",
        "# 1. Bar plot comparing the average Effectiveness for each drug across different regions\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.barplot(x='Product', y='Effectiveness', hue='Region', data=df, ci=None)\n",
        "plt.title('Average Effectiveness by Drug and Region')\n",
        "plt.ylabel('Average Effectiveness')\n",
        "plt.xlabel('Drug')\n",
        "plt.xticks(rotation=45)\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# 2. Violin plot to show the distribution of Effectiveness and Side_Effects for each product\n",
        "plt.figure(figsize=(12, 6))\n",
        "sns.violinplot(x='Product', y='Effectiveness', data=df, inner='quart')\n",
        "sns.violinplot(x='Product', y='Side_Effects', data=df, inner='quart', color='lightgray')\n",
        "plt.title('Effectiveness and Side Effects Distribution by Product')\n",
        "plt.ylabel('Scores')\n",
        "plt.xlabel('Product')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# 3. Pairplot to explore relationships between Effectiveness, Side_Effects, and Marketing_Spend\n",
        "sns.pairplot(df[['Effectiveness', 'Side_Effects', 'Marketing_Spend']])\n",
        "plt.suptitle('Pairplot: Effectiveness, Side Effects, Marketing Spend', y=1.02)\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# 4. Boxplot comparing Effectiveness for different trial periods\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.boxplot(x='Trial_Period', y='Effectiveness', data=df)\n",
        "plt.title('Effectiveness Distribution by Trial Period')\n",
        "plt.ylabel('Effectiveness')\n",
        "plt.xlabel('Trial Period')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# 5. Regression plot to analyze how Marketing_Spend affects drug Effectiveness\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.regplot(x='Marketing_Spend', y='Effectiveness', data=df, scatter_kws={'s': 50}, line_kws={'color': 'red'})\n",
        "plt.title('Effectiveness vs Marketing Spend')\n",
        "plt.xlabel('Marketing Spend')\n",
        "plt.ylabel('Effectiveness')\n",
        "plt.tight_layout()\n",
        "plt.show\n"
      ],
      "metadata": {
        "id": "0rXUouyQovvI",
        "outputId": "c33f99ed-9966-4e8d-dbb4-2e4d60d24371",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        }
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "[Errno 2] No such file or directory: 'drug_data.csv'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-11-e7dd2500015d>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;31m# Load the dataset (make sure to replace the path with the actual path of your dataset)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;31m# Assuming dataset is in a CSV file format\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'drug_data.csv'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;31m# Data Cleaning (check for missing values, data types, and basic cleaning)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36mread_csv\u001b[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[0m\n\u001b[1;32m   1024\u001b[0m     \u001b[0mkwds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkwds_defaults\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1025\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1026\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1027\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1028\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_read\u001b[0;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[1;32m    618\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    619\u001b[0m     \u001b[0;31m# Create the parser.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 620\u001b[0;31m     \u001b[0mparser\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    621\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    622\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[1;32m   1618\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1619\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhandles\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mIOHandles\u001b[0m \u001b[0;34m|\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1620\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1621\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1622\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[0;34m(self, f, engine)\u001b[0m\n\u001b[1;32m   1878\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0;34m\"b\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mmode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1879\u001b[0m                     \u001b[0mmode\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;34m\"b\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1880\u001b[0;31m             self.handles = get_handle(\n\u001b[0m\u001b[1;32m   1881\u001b[0m                 \u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1882\u001b[0m                 \u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/common.py\u001b[0m in \u001b[0;36mget_handle\u001b[0;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[1;32m    871\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mencoding\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0;34m\"b\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    872\u001b[0m             \u001b[0;31m# Encoding\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 873\u001b[0;31m             handle = open(\n\u001b[0m\u001b[1;32m    874\u001b[0m                 \u001b[0mhandle\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    875\u001b[0m                 \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'drug_data.csv'"
          ]
        }
      ]
    }
  ]
}