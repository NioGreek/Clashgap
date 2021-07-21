## Clashgap

[![Version](https://img.shields.io/pypi/v/clashgap?label=version)](https://pypi.org/project/clashgap)
[![Downloads](https://pepy.tech/badge/clashgap/month)](https://pepy.tech/project/clashgap)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue.svg)](http://makeapullrequest.com)
[![Tests](https://github.com/NioGreek/Clashgap/actions/workflows/pytest.yml/badge.svg)](https://github.com/NioGreek/Clashgap/actions)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ad33454aad9d4847ba0a8d1ca3ae2500)](https://app.codacy.com/gh/NioGreek/Clashgap)

A per-charecter diff/compression algorithm implementation in python

### How it works
In case if you have two strings:
> "This is a sentence..." and "This is a word..."

you could "clash" both of them together and find their gap, to get an array loking something like:
> \["This is a", \["sentence", "word"\], "..."\]

As you can the clashgap algorithm looks for collisions in the two strings to find the gap. The clashgaped string maybe used for compression or as the diff of the input strings
