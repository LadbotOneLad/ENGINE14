export default {
  openai: {
    baseURL: 'http://localhost:1234/v1',
    apiKey: 'lm-studio',
    model: 'local-model'
  },
  generator: {
    numComments: 10,
    topics: ['250GHz signal stability', 'Zigbee mesh latency'],
    commentTypes: ['Technical Log', 'Simulation Result']
  }
};
