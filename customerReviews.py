{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOiLgcTDmSbjaY7Nr5EJ9km",
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
        "<a href=\"https://colab.research.google.com/github/Charithareddy22/charithareddy/blob/main/customerReviews.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.impute import SimpleImputer\n",
        "from sklearn.preprocessing import LabelEncoder\n",
        "\n",
        "# Load the dataset\n",
        "df = pd.read_csv('customer_reviews.csv')\n",
        "\n",
        "# Display the first few rows of the dataset\n",
        "print(\"Initial Data:\")\n",
        "print(df.head())\n",
        "\n",
        "# 1. Handle missing values\n",
        "\n",
        "# a) Identify missing values\n",
        "print(\"\\nMissing Values:\")\n",
        "print(df.isnull().sum())\n",
        "\n",
        "# b) Impute missing numerical values for 'Rating' and 'Customer_Age'\n",
        "imputer = SimpleImputer(strategy='mean')\n",
        "df['Rating'] = imputer.fit_transform(df[['Rating']])\n",
        "df['Customer_Age'] = imputer.fit_transform(df[['Customer_Age']])\n",
        "\n",
        "# c) Handle missing textual data in 'Review_Text' using NLP-based techniques (imputing with 'Unknown')\n",
        "df['Review_Text'].fillna('Unknown', inplace=True)\n",
        "\n",
        "print(\"\\nData after imputing missing values:\")\n",
        "print(df.isnull().sum())\n",
        "\n",
        "# 2. Detect and Remove Duplicates\n",
        "# Check for duplicates\n",
        "duplicates = df[df.duplicated()]\n",
        "print(\"\\nDuplicate Rows:\")\n",
        "print(duplicates)\n",
        "\n",
        "# Remove duplicates\n",
        "df = df.drop_duplicates()\n",
        "\n",
        "# 3. Handle Inconsistent Data\n",
        "\n",
        "# a) Standardize Rating values (ensure they range between 1-5)\n",
        "df['Rating'] = df['Rating'].apply(lambda x: max(1, min(5, x)))\n",
        "\n",
        "# b) Correct spelling inconsistencies in Tour_Package names (convert to lowercase and strip spaces)\n",
        "df['Tour_Package'] = df['Tour_Package'].str.lower().str.strip()\n",
        "\n",
        "# 4. Identify and Handle Outliers\n",
        "\n",
        "# a) Use boxplots to find anomalies in 'Package_Price' and 'Rating'\n",
        "sns.boxplot(x=df['Package_Price'])\n",
        "plt.title('Package Price Outliers')\n",
        "plt.show()\n",
        "\n",
        "sns.boxplot(x=df['Rating'])\n",
        "plt.title('Rating Outliers')\n",
        "plt.show()\n",
        "\n",
        "# b) Handling outliers by transforming values (e.g., winsorizing) if necessary\n",
        "# For Package_Price, cap values above the 95th percentile\n",
        "price_upper_limit = df['Package_Price'].quantile(0.95)\n",
        "df['Package_Price'] = np.where(df['Package_Price'] > price_upper_limit, price_upper_limit, df['Package_Price'])\n",
        "\n",
        "# 5. Prepare cleaned data for analysis\n",
        "\n",
        "# a) Convert categorical data into numerical format where required (e.g., 'Rating' can stay as is, 'Tour_Package' needs encoding)\n",
        "label_encoder = LabelEncoder()\n",
        "df['Tour_Package'] = label_encoder.fit_transform(df['Tour_Package'])\n",
        "\n",
        "# 6. Save the cleaned dataset\n",
        "df.to_csv('cleaned_customer_reviews.csv', index=False)\n",
        "\n",
        "print(\"\\nCleaned Data Saved!\")\n",
        "print(df.head())\n"
      ],
      "metadata": {
        "id": "2oiQU57klT7A",
        "outputId": "65dfbe97-cb35-4d81-c047-296e781a1f31",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        }
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "[Errno 2] No such file or directory: 'customer_reviews.csv'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-10-f232f2d4b607>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;31m# Load the dataset\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'customer_reviews.csv'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;31m# Display the first few rows of the dataset\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36mread_csv\u001b[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[0m\n\u001b[1;32m   1024\u001b[0m     \u001b[0mkwds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkwds_defaults\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1025\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1026\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1027\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1028\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_read\u001b[0;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[1;32m    618\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    619\u001b[0m     \u001b[0;31m# Create the parser.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 620\u001b[0;31m     \u001b[0mparser\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    621\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    622\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[1;32m   1618\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1619\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhandles\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mIOHandles\u001b[0m \u001b[0;34m|\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1620\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1621\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1622\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[0;34m(self, f, engine)\u001b[0m\n\u001b[1;32m   1878\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0;34m\"b\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mmode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1879\u001b[0m                     \u001b[0mmode\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;34m\"b\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1880\u001b[0;31m             self.handles = get_handle(\n\u001b[0m\u001b[1;32m   1881\u001b[0m                 \u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1882\u001b[0m                 \u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pandas/io/common.py\u001b[0m in \u001b[0;36mget_handle\u001b[0;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[1;32m    871\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mencoding\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0;34m\"b\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    872\u001b[0m             \u001b[0;31m# Encoding\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 873\u001b[0;31m             handle = open(\n\u001b[0m\u001b[1;32m    874\u001b[0m                 \u001b[0mhandle\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    875\u001b[0m                 \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'customer_reviews.csv'"
          ]
        }
      ]
    }
  ]
}