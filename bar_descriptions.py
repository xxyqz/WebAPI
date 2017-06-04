import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS

my_style=LS(base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)

chart.title='Python Projects'
chart.x_labels=['awesome-python','httpie','thefuck']

plot_dicts=[
    {'value':34600,'label':'Description of awesome-python.'},
    {'value':29895,'label':'Description of httpie.'},
    {'value':28250,'label':'Description of thefuck.'},
]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')