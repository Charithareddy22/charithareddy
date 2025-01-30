{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPFVfaCXJJp1YxIZm8hPgpY",
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
        "<a href=\"https://colab.research.google.com/github/Charithareddy22/charithareddy/blob/main/missdataEcom.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.impute import KNNImputer\n",
        "\n",
        "\n",
        "df = pd.read_csv('C:\\Users\\G.CHARITHA\\Downloads')\n",
        "\n",
        "\n",
        "missing_data = df.isna().sum()\n",
        "print(\"Missing Data Summary:\\n\", missing_data)\n",
        "\n",
        "print(\"\\nDataset Info:\\n\")\n",
        "df.info()\n",
        "\n",
        "\n",
        "missing_percentage = (df.isna().sum() / len(df)) * 100\n",
        "print(\"\\nPercentage of Missing Data for Each Column:\\n\", missing_percentage)\n",
        "\n",
        "\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.heatmap(df.isna(), cbar=False, cmap='viridis', yticklabels=False)\n",
        "plt.title('Missing Data Heatmap')\n",
        "plt.show()\n",
        "\n",
        "\n",
        "df['Product_Price'] = df['Product_Price'].fillna(df['Product_Price'].median())\n",
        "\n",
        "\n",
        "df['Product_Category'] = df['Product_Category'].fillna(df['Product_Category'].mode()[0])\n",
        "\n",
        "\n",
        "df['Order_Date'] = df['Order_Date'].fillna(method='ffill')\n",
        "\n",
        "\n",
        "knn_imputer = KNNImputer(n_neighbors=5)\n",
        "numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns\n",
        "df[numerical_cols] = knn_imputer.fit_transform(df[numerical_cols])\n",
        "\n",
        "print(\"\\nSummary Statistics Before Imputation:\\n\", df.describe())\n",
        "df_imputed = df.copy()\n",
        "\n",
        "plt.figure(figsize=(10, 6))\n",
        "plt.subplot(1, 2, 1)\n",
        "df['Product_Price'].hist(bins=20, color='skyblue', edgecolor='black')\n",
        "plt.title('Product Price Distribution Before Imputation')\n",
        "\n",
        "plt.subplot(1, 2, 2)\n",
        "df_imputed['Product_Price'].hist(bins=20, color='lightcoral', edgecolor='black')\n",
        "plt.title('Product Price Distribution After Imputation')\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "\n",
        "df.to_csv('cleaned_ecommerce_orders.csv', index=False)\n"
      ],
      "metadata": {
        "id": "oa8V4Iqoi-3T",
        "outputId": "d9464a5b-ae13-45e6-bb6e-ed242d9eb682",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        }
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \\UXXXXXXXX escape (<ipython-input-9-298db75cbbc3>, line 8)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-9-298db75cbbc3>\"\u001b[0;36m, line \u001b[0;32m8\u001b[0m\n\u001b[0;31m    df = pd.read_csv('C:\\Users\\G.CHARITHA\\Downloads')\u001b[0m\n\u001b[0m                                                    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \\UXXXXXXXX escape\n"
          ]
        }
      ]
    }
  ]
}