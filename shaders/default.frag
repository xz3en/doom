#version 330 core
out vec4 fragment;

void main()
{
    vec3 albedo = vec3(1.0,0.0,0.0);
    fragment = vec4(albedo,1.0);
} 