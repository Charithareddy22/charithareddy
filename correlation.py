{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Charithareddy22/charithareddy/blob/main/correlation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "# Define the dataset\n",
        "x = np.array([1,3,5,7,8,9, 10, 15])\n",
        "y = np.array([10, 20, 30, 40, 50, 60, 70, 80])\n",
        "def Pearson_correlation(X,Y):\n",
        "\tif len(X)==len(Y):\n",
        "\t\tSum_xy = sum((X-X.mean())*(Y-Y.mean()))\n",
        "\t\tSum_x_squared = sum((X-X.mean())**2)\n",
        "\t\tSum_y_squared = sum((Y-Y.mean())**2)\n",
        "\t\tcorr = Sum_xy / np.sqrt(Sum_x_squared * Sum_y_squared)\n",
        "\treturn corr\n",
        "\n",
        "print(Pearson_correlation(x,y))\n",
        "print(Pearson_correlation(x,x))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nXmxZewpmGqK",
        "outputId": "3a0658bb-19ba-4d79-a51b-6a5ac6684199"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.974894414261588\n",
            "1.0\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMcpa+LvWZNT7bwBqoKZwiI",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}