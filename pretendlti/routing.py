from channels.routing import route, route_class
from numbas_lti import consumers

channel_routing = [
    route("websocket.receive",consumers.scorm_set_element, path=r'^/websocket/attempt/(?P<pk>\d+)/scorm_api$'),
    route_class(consumers.AttemptScormListingConsumer, path=r'^/websocket/attempt/(?P<pk>\d+)/scorm_listing$'),
    route("report.all_scores",consumers.report_scores),
    route("editorlink.update_cache",consumers.update_editorlink),
]
