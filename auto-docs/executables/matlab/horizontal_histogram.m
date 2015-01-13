% Learn about API authentication here: {{BASE_URL}}/matlab/getting-started
% Find your api_key here: {{BASE_URL}}/settings/api

y = randn(500,1);

signin('TestBot', 'r1neazxo9w')
data = {...
  struct(...
    'y', y, ...
    'type', 'histogram')...
};
response = plotly(data, struct('filename', 'horizontal-histogram', 'fileopt', 'overwrite'));
plot_url = response.url
