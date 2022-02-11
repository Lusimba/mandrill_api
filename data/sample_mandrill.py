import json

sample_data = [
  {
    "event": "open",
    "msg": {
      "ts": 1365109999,
      "subject": "Roses Are Red, Violets Are On Sale",
      "email": "flowerfriend@example.com",
      "sender": "hello@eiffelflowers.biz",
      "tags": ["violets"],
      "opens": [
        {
          "ts": 1365111111
        }
      ],
      "clicks": [
        {
          "ts": 1365111111,
          "url": "https://www.eiffelflowers.biz/news/ultraviolet-sale"
        }
      ],
      "state": "sent",
      "metadata": {
        "user_id": 111
      },
      "_id": "123",
      "_version": "123"
    },
    "_id": "1121",
    "ts": 1382434004
  },
  {
    "event": "send",
    "msg": {
      "ts": 1365109999,
      "subject": "This an example webhook message",
      "email": "carol.webhook@mandrillapp.com",
      "sender": "example.sender@mandrillapp.com",
      "tags": [
        "webhook-example"
      ],
      "opens": [
        
      ],
      "clicks": [
        
      ],
      "state": "sent",
      "metadata": {
        "user_id": 111
      },
      "_id": "124",
      "_version": "123"
    },
    "_id": "1122",
    "ts": 1384954004
  },
  {
    "event": "deferral",
    "msg": {
      "ts": 1365109999,
      "subject": "This an example webhook message",
      "email": "james.webhook@mandrillapp.com",
      "sender": "example.sender@mandrillapp.com",
      "tags": [
        "webhook-example"
      ],
      "opens": [
        
      ],
      "clicks": [
        
      ],
      "state": "deferred",
      "metadata": {
        "user_id": 111
      },
      "_id": "1130",
      "_version": "123",
      "smtp_events": [
        {
          "destination_ip": "127.0.0.1",
          "diag": "451 4.3.5 Temporarily unavailable, try again later.",
          "source_ip": "127.0.0.1",
          "ts": 1365111111,
          "type": "deferred",
          "size": 0
        }
      ]
    },
    "_id": "1123",
    "ts": 1384954004
  },
  {
    "event": "hard_bounce",
    "msg": {
      "ts": 1365109999,
      "subject": "This an example webhook message",
      "email": "raymond.webhook@mandrillapp.com",
      "sender": "example.sender@mandrillapp.com",
      "tags": [
        "webhook-example"
      ],
      "state": "bounced",
      "metadata": {
        "user_id": 111
      },
      "_id": "113",
      "_version": "123",
      "bounce_description": "bad_mailbox",
      "bgtools_code": 10,
      "diag": "smtp;550 5.1.1 The email account that you tried to reach does not exist. Please try double-checking the recipient's email address for typos or unnecessary spaces."
    },
    "_id": "1124",
    "ts": 1384954004
  },
  {
    "event": "soft_bounce",
    "msg": {
      "ts": 1365109999,
      "subject": "This an example webhook message",
      "email": "harvey.webhook@mandrillapp.com",
      "sender": "example.sender@mandrillapp.com",
      "tags": [
        "webhook-example"
      ],
      "state": "soft-bounced",
      "metadata": {
        "user_id": 111
      },
      "_id": "1203",
      "_version": "165",
      "bounce_description": "mailbox_full",
      "bgtools_code": 22,
      "diag": "smtp;552 5.2.2 Over Quota"
    },
    "_id": "1124",
    "ts": 1384954004
  },
  {
    "event": "open",
    "msg": {
      "ts": 1365109999,
      "subject": "This an example webhook message",
      "email": "ashley.webhook@mandrillapp.com",
      "sender": "example.sender@mandrillapp.com",
      "tags": [
        "webhook-example"
      ],
      "opens": [
        {
          "ts": 1365111111
        }
      ],
      "clicks": [
        {
          "ts": 1365111111,
          "url": "http://mandrill.com"
        }
      ],
      "state": "sent",
      "metadata": {
        "user_id": 111
      },
      "_id": "1126",
      "_version": "124"
    },
    "_id": "1127",
    "ip": "127.0.0.1",
    "location": {
      "country_short": "US",
      "country": "United States",
      "region": "Oklahoma",
      "city": "Oklahoma City",
      "latitude": 35.4675598145,
      "longitude": -97.5164337158,
      "postal_code": "73101",
      "timezone": "-05:00"
    },
    "user_agent": "Mozilla//5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1.8) Gecko//20100317 Postbox/1.1.3",
    "user_agent_parsed": {
      "type": "Email Client",
      "ua_family": "Postbox",
      "ua_name": "Postbox 1.1.3",
      "ua_version": "1.1.3",
      "ua_url": "http://www.postbox-inc.com/",
      "ua_company": "Postbox, Inc.",
      "ua_company_url": "http:\/\/www.postbox-inc.com\/",
      "ua_icon": "http://cdn.mandrill.com/img/email-client-icons/postbox.png",
      "os_family": "OS X",
      "os_name": "OS X 10.6 Snow Leopard",
      "os_url": "http://www.apple.com/osx/",
      "os_company": "Apple Computer, Inc.",
      "os_company_url": "http://www.apple.com/",
      "os_icon": "http://cdn.mandrill.com/img/email-client-icons/macosx.png",
      "mobile": False
    },
    "ts": 1384954004
  },
  {
    "event": "click",
    "msg": {
      "ts": 1365109999,
      "subject": "This an example webhook message",
      "email": "rachel.webhook@mandrillapp.com",
      "sender": "example.sender@mandrillapp.com",
      "tags": [
        "webhook-example"
      ],
      "opens": [
        {
          "ts": 1365111111
        }
      ],
      "clicks": [
        {
          "ts": 1365111111,
          "url": "http://mandrill.com"
        }
      ],
      "state": "sent",
      "metadata": {
        "user_id": 111
      },
      "_id": "1128",
      "_version": "123"
    },
    "_id": "1129",
    "ip": "127.0.0.1",
    "location": {
      "country_short": "US",
      "country": "United States",
      "region": "Oklahoma",
      "city": "Oklahoma City",
      "latitude": 35.4675598145,
      "longitude": -97.5164337158,
      "postal_code": "73101",
      "timezone": "-05:00"
    },
    "user_agent": "Mozilla\/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1.8) Gecko\/20100317 Postbox\/1.1.3",
    "user_agent_parsed": {
      "type": "Email Client",
      "ua_family": "Postbox",
      "ua_name": "Postbox 1.1.3",
      "ua_version": "1.1.3",
      "ua_url": "http://www.postbox-inc.com\/",
      "ua_company": "Postbox, Inc.",
      "ua_company_url": "http://www.postbox-inc.com\/",
      "ua_icon": "http://cdn.mandrill.com\/img\/email-client-icons\/postbox.png",
      "os_family": "OS X",
      "os_name": "OS X 10.6 Snow Leopard",
      "os_url": "http://www.apple.com\/osx\/",
      "os_company": "Apple Computer, Inc.",
      "os_company_url": "http://www.apple.com\/",
      "os_icon": "http://cdn.mandrill.com/img/email-client-icons/macosx.png",
      "mobile": False
    },
    "url": "http://mandrill.com",
    "ts": 1384954004
  },
  {
    "event": "spam",
    "msg": {
      "ts": 1365109999,
      "subject": "This an example webhook message",
      "email": "pamela.webhook@mandrillapp.com",
      "sender": "example.sender@mandrillapp.com",
      "tags": [
        "webhook-example"
      ],
      "opens": [
        {
          "ts": 1365111111
        }
      ],
      "clicks": [
        {
          "ts": 1365111111,
          "url": "http://mandrill.com"
        }
      ],
      "state": "sent",
      "metadata": {
        "user_id": 111
      },
      "_id": "1131",
      "_version": "123"
    },
    "_id": "1131",
    "ts": 1384954004
  },
  {
    "event": "unsub",
    "msg": {
      "ts": 1365109999,
      "subject": "This an example webhook message",
      "email": "robbin.webhook@mandrillapp.com",
      "sender": "example.sender@mandrillapp.com",
      "tags": [
        "webhook-example"
      ],
      "opens": [
        {
          "ts": 1365111111
        }
      ],
      "clicks": [
        {
          "ts": 1365111111,
          "url": "http://mandrill.com"
        }
      ],
      "state": "sent",
      "metadata": {
        "user_id": 111
      },
      "_id": "1132",
      "_version": "123"
    },
    "_id": "1133",
    "ts": 1384954004
  },
  {
    "event": "reject",
    "msg": {
      "ts": 1365109999,
      "subject": "This an example webhook message",
      "email": "andy.webhook@mandrillapp.com",
      "sender": "example.sender@mandrillapp.com",
      "tags": [
        "webhook-example"
      ],
      "opens": [
        
      ],
      "clicks": [
        
      ],
      "state": "rejected",
      "metadata": {
        "user_id": 111
      },
      "_id": "1135",
      "_version": "123"
    },
    "_id": "1140",
    "ts": 1384954004
  }
]


# convert the dictionary data to JSON
mandrill_data = json.dumps(sample_data)