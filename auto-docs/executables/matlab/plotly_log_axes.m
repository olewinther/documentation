% Learn about API authentication here: {{BASE_URL}}/matlab/getting-started
% Find your api_key here: {{BASE_URL}}/settings/api

signin('TestBot', 'r1neazxo9w')
trace1 = struct(...
  'x', [0, 1, 2, 3, 4, 5, 6, 7, 8], ...
  'y', [8, 7, 6, 5, 4, 3, 2, 1, 0], ...
  'type', 'scatter');
trace2 = struct(...
  'x', [0, 1, 2, 3, 4, 5, 6, 7, 8], ...
  'y', [0, 1, 2, 3, 4, 5, 6, 7, 8], ...
  'type', 'scatter');
data = {trace1, trace2};
layout = struct(...
    'xaxis', struct(...
      'type', 'log', ...
      'autorange', true), ...
    'yaxis', struct(...
      'type', 'log', ...
      'autorange', true));
response = plotly(data, struct('layout', layout, 'filename', 'plotly-log-axes', 'fileopt', 'overwrite'));
plot_url = response.url
