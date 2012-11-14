#!/bin/bash
############ member category
curl -X POST -d@post_category_cmbs_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/-/
curl -X PUT -d@put_provider_cmbs_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json'  -v http://127.0.0.1:8090/-/

############ message category
curl -X POST -d@post_category_cmbs_message.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/-/
curl -X PUT -d@put_provider_cmbs_message.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/-/

############ member instance
curl -X POST -d@post_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/
curl -X POST -d@action_check_neighbors_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=check_neighbors
curl -X POST -d@action_start_l1_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=start_l1
#curl -X POST -d@action_stop_l1_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=stop_l1
curl -X POST -d@action_start_l2_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=start_l2
#curl -X POST -d@action_stop_l2_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=stop_l2
#curl -X POST -d@action_start_l31_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=start_l31
#curl -X POST -d@action_stop_l31_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=stop_l31
#curl -X POST -d@action_start_l32_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=start_l32
#curl -X POST -d@action_stop_l32_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=stop_l32
#curl -X POST -d@action_start_l4_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=start_l4
#curl -X POST -d@action_stop_l4_member.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/member/016ad860-2a9a-504f-8861-aeafd0b2ae29?action=stop_l4

############ message L1 instance
#curl -X POST -d@post_message_l1.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/message/
#curl -X POST -d@action_send_l1_message.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/message/0101d860-2a9a-504f-8861-aeafd0b20101?action=send_l1

############ message L2 instance
#curl -X POST -d@post_message_l2.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/message/
#curl -X POST -d@action_send_l2_message.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/message/0102d860-2a9a-504f-8861-aeafd0a10201?action=send_l2

#curl -X POST -d@post_message_l31.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/message/
#curl -X POST -d@post_message_l32.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/message/
#curl -X POST -d@post_message_l4.json -H 'content-type: application/occi+json' -H 'accept: application/occi+json' -v http://127.0.0.1:8090/cmbs/message/
