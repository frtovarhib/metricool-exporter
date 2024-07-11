from modules.MetricoolService import client

max_profiles = client.get('/admin/max-profiles', params={})
print(max_profiles)

simple_profiles = client.get('/admin/simpleProfiles', params={})
print(simple_profiles)

profiles_auth = client.get('/admin/profiles-auth', params={})
print(profiles_auth)
