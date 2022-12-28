from pretty_html_table import build_table

def convert_to_html(dataframe):
    output = build_table(dataframe, 'green_light')
    return output