% Learn about API authentication here: {{BASE_URL}}/matlab/getting-started
% Find your api_key here: {{BASE_URL}}/settings/api

signin('TestBot', 'r1neazxo9w')
data = {...
  struct(...
    'x', [1, 2, 3, 4], ...
    'y', [2, 1, 3, 4], ...
    'error_y', struct(...
      'type', 'percent', ...
      'symmetric', false, ...
      'value', 15, ...
      'valueminus', 25), ...
    'type', 'scatter')...
};
response = plotly(data, struct('filename', 'error-bar-asymmetric-constant', 'fileopt', 'overwrite'));
plot_url = response.url
