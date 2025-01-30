{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM9MuYBolhUAvR6obaCadR7",
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
        "<a href=\"https://colab.research.google.com/github/Charithareddy22/charithareddy/blob/main/minmaxscaler.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "from sklearn.preprocessing import MinMaxScaler\n",
        "\n",
        "# Create the DataFrame\n",
        "data = {\n",
        "    \"age\": [10, 15, 20, 25, 30],\n",
        "    \"height\": [100, 200, 250, 300, 150],\n",
        "    \"weight\": [45, 50, 55, 60, 65],\n",
        "}\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "# Initialize the MinMaxScaler\n",
        "scaler = MinMaxScaler()\n",
        "\n",
        "# Normalize the data\n",
        "normalized_data = scaler.fit_transform(df)\n",
        "\n",
        "# Convert the normalized data back to a DataFrame\n",
        "normalized_df = pd.DataFrame(normalized_data, columns=df.columns)\n",
        "\n",
        "# Print the normalized DataFrame\n",
        "print(\"\\nNormalized DataFrame (scaled to range [0, 1]):\")\n",
        "print(normalized_df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6-Y1xXtof-Wi",
        "outputId": "96aa6245-fd0c-4fb7-dbcd-defe8bd060c9"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Normalized DataFrame (scaled to range [0, 1]):\n",
            "    age  height  weight\n",
            "0  0.00    0.00    0.00\n",
            "1  0.25    0.50    0.25\n",
            "2  0.50    0.75    0.50\n",
            "3  0.75    1.00    0.75\n",
            "4  1.00    0.25    1.00\n"
          ]
        }
      ]
    }
  ]
}