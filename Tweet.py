{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM7bWJxOrBNPbOgG2RHH6er",
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
        "<a href=\"https://colab.research.google.com/github/salonikumari08/Big_Mart_Sales_Prediction/blob/main/Tweet.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "cfDQxGPlQ--m"
      },
      "outputs": [],
      "source": [
        "#Using pandas for loading and handling the data\n",
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Reading the smaller file for simplicity (same approach for larger file in chunks)\n",
        "file_path = '/content/correct_twitter_201904 (1).tsv'\n",
        "df = pd.read_csv(file_path, sep='\\t')"
      ],
      "metadata": {
        "id": "OKgqaau0ROV9"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Top five rows of data\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 429
        },
        "id": "k0IKp8UQTj3p",
        "outputId": "6f3549cc-ac5b-4663-e7ee-b1ca5d6afa4e"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                    id           event                               ts1  \\\n",
              "0  1131594960443199488  britney_201904  2022-02-28 09:34:44.627023-05:00   \n",
              "1  1131594976750653440  britney_201904  2022-02-28 09:34:44.626921-05:00   \n",
              "2  1131589737955942405  britney_201904  2022-02-28 09:34:44.634058-05:00   \n",
              "3  1131594909469892610  britney_201904  2022-02-28 09:34:44.627125-05:00   \n",
              "4  1131594812694511617  britney_201904  2022-02-28 09:34:44.627227-05:00   \n",
              "\n",
              "                                ts2  from_stream  directly_from_stream  \\\n",
              "0  2022-02-28 09:34:44.627023-05:00         True                  True   \n",
              "1  2022-02-28 09:34:44.626921-05:00         True                  True   \n",
              "2  2022-02-28 09:34:44.634058-05:00         True                  True   \n",
              "3  2022-02-28 09:34:44.627125-05:00         True                  True   \n",
              "4  2022-02-28 09:34:44.627227-05:00         True                  True   \n",
              "\n",
              "   from_search  directly_from_search  from_quote_search  \\\n",
              "0        False                 False              False   \n",
              "1        False                 False              False   \n",
              "2        False                 False              False   \n",
              "3        False                 False              False   \n",
              "4        False                 False              False   \n",
              "\n",
              "   directly_from_quote_search  ...     retweeted  retweeted_author_id  \\\n",
              "0                       False  ...  1.130918e+18         3.042894e+09   \n",
              "1                       False  ...           NaN                  NaN   \n",
              "2                       False  ...           NaN                  NaN   \n",
              "3                       False  ...  1.130918e+18         3.042894e+09   \n",
              "4                       False  ...  1.130918e+18         3.042894e+09   \n",
              "\n",
              "   retweeted_handle  retweeted_follower_count mentioned_author_ids  \\\n",
              "0          Iesbwian                   22760.0                  NaN   \n",
              "1               NaN                       NaN                  NaN   \n",
              "2               NaN                       NaN                  NaN   \n",
              "3          Iesbwian                   22760.0                  NaN   \n",
              "4          Iesbwian                   22760.0                  NaN   \n",
              "\n",
              "  mentioned_handles  hashtags urls media_keys  place_id  \n",
              "0               NaN       NaN  NaN        NaN       NaN  \n",
              "1               NaN       NaN  NaN        NaN       NaN  \n",
              "2               NaN       NaN  NaN        NaN       NaN  \n",
              "3               NaN       NaN  NaN        NaN       NaN  \n",
              "4               NaN       NaN  NaN        NaN       NaN  \n",
              "\n",
              "[5 rows x 46 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-7ea68e00-4917-4d91-b6e7-475794aa4515\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>event</th>\n",
              "      <th>ts1</th>\n",
              "      <th>ts2</th>\n",
              "      <th>from_stream</th>\n",
              "      <th>directly_from_stream</th>\n",
              "      <th>from_search</th>\n",
              "      <th>directly_from_search</th>\n",
              "      <th>from_quote_search</th>\n",
              "      <th>directly_from_quote_search</th>\n",
              "      <th>...</th>\n",
              "      <th>retweeted</th>\n",
              "      <th>retweeted_author_id</th>\n",
              "      <th>retweeted_handle</th>\n",
              "      <th>retweeted_follower_count</th>\n",
              "      <th>mentioned_author_ids</th>\n",
              "      <th>mentioned_handles</th>\n",
              "      <th>hashtags</th>\n",
              "      <th>urls</th>\n",
              "      <th>media_keys</th>\n",
              "      <th>place_id</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1131594960443199488</td>\n",
              "      <td>britney_201904</td>\n",
              "      <td>2022-02-28 09:34:44.627023-05:00</td>\n",
              "      <td>2022-02-28 09:34:44.627023-05:00</td>\n",
              "      <td>True</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>...</td>\n",
              "      <td>1.130918e+18</td>\n",
              "      <td>3.042894e+09</td>\n",
              "      <td>Iesbwian</td>\n",
              "      <td>22760.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1131594976750653440</td>\n",
              "      <td>britney_201904</td>\n",
              "      <td>2022-02-28 09:34:44.626921-05:00</td>\n",
              "      <td>2022-02-28 09:34:44.626921-05:00</td>\n",
              "      <td>True</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1131589737955942405</td>\n",
              "      <td>britney_201904</td>\n",
              "      <td>2022-02-28 09:34:44.634058-05:00</td>\n",
              "      <td>2022-02-28 09:34:44.634058-05:00</td>\n",
              "      <td>True</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1131594909469892610</td>\n",
              "      <td>britney_201904</td>\n",
              "      <td>2022-02-28 09:34:44.627125-05:00</td>\n",
              "      <td>2022-02-28 09:34:44.627125-05:00</td>\n",
              "      <td>True</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>...</td>\n",
              "      <td>1.130918e+18</td>\n",
              "      <td>3.042894e+09</td>\n",
              "      <td>Iesbwian</td>\n",
              "      <td>22760.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1131594812694511617</td>\n",
              "      <td>britney_201904</td>\n",
              "      <td>2022-02-28 09:34:44.627227-05:00</td>\n",
              "      <td>2022-02-28 09:34:44.627227-05:00</td>\n",
              "      <td>True</td>\n",
              "      <td>True</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>...</td>\n",
              "      <td>1.130918e+18</td>\n",
              "      <td>3.042894e+09</td>\n",
              "      <td>Iesbwian</td>\n",
              "      <td>22760.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 46 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7ea68e00-4917-4d91-b6e7-475794aa4515')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-7ea68e00-4917-4d91-b6e7-475794aa4515 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-7ea68e00-4917-4d91-b6e7-475794aa4515');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-93a75525-7b65-4f30-aa4f-abbe86d27b1e\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-93a75525-7b65-4f30-aa4f-abbe86d27b1e')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-93a75525-7b65-4f30-aa4f-abbe86d27b1e button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# To check the columns of data\n",
        "df.columns"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1L-9d3QWZFr-",
        "outputId": "0ff05631-e113-4d9e-b7da-4271eb6d6216"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['id', 'event', 'ts1', ' ts2', 'from_stream', 'directly_from_stream',\n",
              "       'from_search', 'directly_from_search', 'from_quote_search',\n",
              "       'directly_from_quote_search', 'from_convo_search',\n",
              "       'directly_from_convo_search', 'from_timeline_search',\n",
              "       'directly_from_timeline_search', 'text', 'lang', 'author_id',\n",
              "       'author_handle', 'created_at', 'conversation_id', 'possibly_sensitive',\n",
              "       'reply_settings', 'source', 'author_follower_count', 'retweet_count',\n",
              "       'reply_count', 'like_count', 'quote_count', 'replied_to',\n",
              "       'replied_to_author_id', 'replied_to_handle',\n",
              "       'replied_to_follower_count', 'quoted', 'quoted_author_id',\n",
              "       'quoted_handle', 'quoted_follower_count', 'retweeted',\n",
              "       'retweeted_author_id', 'retweeted_handle', 'retweeted_follower_count',\n",
              "       'mentioned_author_ids', 'mentioned_handles', 'hashtags', 'urls',\n",
              "       'media_keys', 'place_id'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#How many tweets were posted containing the term on each day\n",
        "def tweets_per_day(term, df):\n",
        "    term_df = search_term_data(term, df)\n",
        "    return term_df.groupby(term_df['ts1'].dt.date)['id'].count()"
      ],
      "metadata": {
        "id": "Y6T095qCUGjr"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#How many unique users posted a tweet containing the term\n",
        "def unique_users(term, df):\n",
        "    term_df = search_term_data(term, df)\n",
        "    return term_df['retweeted_author_id'].nunique()"
      ],
      "metadata": {
        "id": "JTR4R_t8VbAl"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#How many likes did tweets containing the term get on average\n",
        "def avg_likes(term, df):\n",
        "    term_df = search_term_data(term, df)\n",
        "    return term_df['likes'].mean()"
      ],
      "metadata": {
        "id": "I_KjzzqFViCl"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Where (in terms of place IDs) did the tweets come from\n",
        "def tweet_places(term, df):\n",
        "    term_df = search_term_data(term, df)\n",
        "    return term_df['place_id'].unique()"
      ],
      "metadata": {
        "id": "JaQBUTazV_yJ"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#What times of day were the tweets posted at\n",
        "def tweet_times(term, df):\n",
        "    term_df = search_term_data(term, df)\n",
        "    term_df['time'] = term_df['date'].dt.time\n",
        "    return term_df['time'].value_counts()"
      ],
      "metadata": {
        "id": "Uq5rs4dMWNpz"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Which user posted the most tweets containing the term\n",
        "def top_user(term, df):\n",
        "    term_df = search_term_data(term, df)\n",
        "    return term_df['user_id'].value_counts().idxmax()"
      ],
      "metadata": {
        "id": "DQ0sp1qjWfZ0"
      },
      "execution_count": 11,
      "outputs": []
    }
  ]
}