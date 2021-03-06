# Copyright (c) 2009 Muh Hon Cheng
# Created by honcheng on 4/12/10.
# 
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the 
# "Software"), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, 
# distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject 
# to the following conditions:
# 
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT 
# WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT 
# SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
# IN CONNECTION WITH THE SOFTWARE OR 
# THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# @author 		Muh Hon Cheng <honcheng@gmail.com>
# @copyright	2010	Muh Hon Cheng
#

# details about Twitter account
# sign up for a twitter account at twitter.com, and then create a twitter application
# using the same twitter account at developer.twitter.com 
# replace the relevant strings below from the newly created twitter application
twitterbot_consumer_key = "insert-consumer-key-here"
twitterbot_consumer_secret = "insert-consumer-secret-here"
twitterbot_access_token = "insert-access-token-here"
twitterbot_access_token_secret = "insert-access-token-secret-here"
# alternative account to use, in case daily 250 quota is exceeded
# have not put this to test yet
twitterbot_access_token_alternative = "276415537-yxCaRVAorBdHHv4jnDFRRlKZABXDQJDzABRVid3x"
twitterbot_access_token_secret_alternative = "vFbGfR6U3nIrPbknm0pPiPaHYkk68H14AGKS6BrY1g"

# details about retry
n_times_to_retry_408_before_sending_alerts = 2

# details about bitly
bitly_username = "insert-bitly-username-here"
bitly_apikey = "insert-bitly-api-key-here"

# details about goo.gl
googl_apikey = 'insert-googl-api-key-here'

# urls
url_track_id = '/apimonitor/track/id'
url_remove = '/apimonitor/remove'
url_check = '/apimonitor/check'
url_track = '/apimonitor/track'
url_add = '/apimonitor/add'
url_addapi = '/apimonitor/addapi'