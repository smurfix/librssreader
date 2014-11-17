# ReadMe
librssreader is based on the original work libgreader from Matthew Behrens <askedrelic@gmail.com>. And it is developer oriented python package. With simple configuration changes and little codes, we hope it would support all Google Reader Api Like Rss Readers like 'Inoreader/The old Reader/Feedly' etc. RSS Reader ain't dead yet! The library will support inoreader by default, and will be easy to extend to support other Rss Reader.

libgreader is a basic configurable Python library for authenticating and interacting with the unofficial Google Reader API. It currently supports all major user authentication methods (ClientLogin, OAuth2) and aims to simplify the many features that Google Reader offers.

Licensed under the MIT license: [http://www.opensource.org/licenses/mit-license.php]()

## Features

* Support for all Google recommended authentication methods, for easy integration with existing web or desktop applications
* Explanation of most of the Google Reader API endpoints, which Google has never really opened up
* Convenient functions and models for working with those endpoints
* A modest integration test suite!

## Usage

It's as simple as:


	>>> from librssreader.inoreader import RssReader, ClientAuthMethod, Item
	>>> auth = ClientAuthMethod('YOUR USERNAME','YOUR PASSWORD')
	>>> reader = RssReader(auth)
	>>> print reader.getUserInfo()
	{u'userName': u'Foo', u'userEmail': u'librssreadertest@gmail.com', u'userId': u'16058940398976999581', u'userProfileId': u'100275409503040726101', u'isBloggerUser': False, u'signupTimeSec': 0, u'isMultiLoginEnabled': False}`

For more examples with all of the authentication methods, see the [USAGE file](https://github.com/askedrelic/libgreader/blob/master/USAGE.md).

## Installation

libgreader is on pypi at [http://pypi.python.org/pypi/libgreader/](http://pypi.python.org/pypi/libgreader/)

	$ pip install librssreader

or 

	$ easy_install librssreader

## Note

The old reader config now *DO NOT* well test and may not work. It now only is an example for how to extend the library to other rssreaders. Any contribution will be appreciated.

## Testing and Contribution

Want to test it out or contribute some changes?

First, fork the repository on Github to make changes on your private branch.
Then, create a dev environment using a virtualenv:

	$ pip install virtualenvwrapper
	$ mkvirtualenv venv-librreader --no-site-packages

Checkout your fork and then run the tests:

	$ python setup.py test

Now hack away! Write tests which show that a bug was fixed or that the feature works as expected. Then send a pull request and bug me until it gets merged in and published.


## Thanks

Originally created from:

[https://github.com/askedrelic/libgreader/](libgreader)
