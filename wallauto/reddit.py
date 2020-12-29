""" This module manages Reddit API """

import praw


class RedditClient:

    def __init__(self, client_id, client_secret, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent

    def _connect(self):
        """ Connects to Reddit. """
        return praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent
        )

    def sub(self, subreddit='EarthPorn', limit=25,
            time_filter='all', secc='top'):
        """ Get post from Subreddit.
        Params:
            subreddit (string): Subreddit name.
            limit (number): amount of post.
            time_filter (string): Can be one of: all, day, hour, month, week,
            year (default: all).
            secc (string): filter to be used.
        """
        sub = self._connect().subreddit(subreddit)
        if secc == 'top':
            return [post for post in sub.top(
                limit=limit,
                time_filter=time_filter
            )]
        elif secc == 'hot':
            return [post for post in sub.top(
                limit=limit,
                time_filter=time_filter
            )]
        elif secc == 'rising':
            return [post for post in sub.rising(
                limit=limit,
            )]
        elif secc == 'new':
            return [post for post in sub.new(
                limit=limit,
            )]
