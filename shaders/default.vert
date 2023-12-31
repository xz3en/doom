#version 330 core
layout (location = 0) in vec3 vertex;

uniform mat4 perspective;
uniform mat4 view;

void main()
{
    gl_Position = perspective * view * vec4(vertex,1.0);
}