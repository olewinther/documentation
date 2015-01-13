% Learn about API authentication here: {{BASE_URL}}/matlab/getting-started
% Find your api_key here: {{BASE_URL}}/settings/api

signin('TestBot', 'r1neazxo9w')
data = {...
  struct(...
    'z', [1, 20, 30, 50, 1; 20, 1, 60, 80, 30; 30, 60, 1, -10, 20], ...
    'x', { {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'} }, ...
    'y', { {'Morning', 'Afternoon', 'Evening'} }, ...
    'type', 'heatmap')...
};
response = plotly(data, struct('filename', 'labelled-heatmap', 'fileopt', 'overwrite'));
plot_url = response.url
