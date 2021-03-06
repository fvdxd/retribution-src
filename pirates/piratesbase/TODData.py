from panda3d.core import Vec3, Vec4
from pirates.piratesbase.TODDefs import *
ENV_SETTINGS_DEFAULT = {
    'BASE': {
        'Direction': Vec3(0, 30, 245),
        'LightSwitch': [
            1,
            1,
            1],
        'FrontColor': Vec4(0, 0, 0, 1),
        'BackColor': Vec4(0, 0, 0, 1),
        'AmbientColor': Vec4(0, 0, 0, 1),
        'FogType': FOG_EXP,
        'FogColor': Vec4(0.25, 0.25, 0.25, 0),
        'FogExp': 0.0001,
        'FogLinearRange': (500.0, 750.0),
        'SkyType': SKY_DAY,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.200, 0.200, 0.200, 1),
        'SeaColorShader': Vec4(0.200, 0.200, 0.200, 1),
        'SeaFactor': Vec3(1.0, 1.0, 1.0),
        'EnvEffect': 0 },
    'Dawn': {
        'Direction': Vec3(0, 35, 330),
        'FrontColor': Vec4(1.5, 1.2, 0.9, 1),
        'BackColor': Vec4(0.348, 0.418, 0.71, 1),
        'AmbientColor': Vec4(0.38, 0.53000, 0.680000, 1),
        'FogColor': Vec4(0.288, 0.320, 0.44, 0),
        'FogExp': 0.00400,
        'SkyType': SKY_DAWN,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.348, 0.5, 0.62, 1),
        'SeaColorShader': Vec4(0.348, 0.348, 0.200, 1) },
    'Day': {
        'FrontColor': Vec4(2, 1.79, 1.47, 1),
        'BackColor': Vec4(0.348, 0.408, 0.62, 1),
        'AmbientColor': Vec4(0.800000, 0.88, 0.930000, 1),
        'FogColor': Vec4(0.598, 0.696, 0.9, 0),
        'FogExp': 0.00060000002849800002,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.299, 0.75, 1, 1),
        'SeaColorShader': Vec4(0.100, 0.25, 0.149, 1) },
    'Dusk': {
        'Direction': Vec3(0, 35, 175),
        'FrontColor': Vec4(1.71, 1.36, 1.14, 1),
        'BackColor': Vec4(0.58, 0.58, 0.88, 1),
        'AmbientColor': Vec4(0.52, 0.390, 0.418, 1),
        'FogColor': Vec4(0.46, 0.38, 0.429, 0),
        'FogExp': 0.00060000002849800002,
        'SkyType': SKY_DUSK,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.348, 0.5, 0.62, 1),
        'SeaColorShader': Vec4(0.25, 0.25, 0.149, 1) },
    'Night': {
        'Direction': Vec3(0, 40, 90),
        'FrontColor': Vec4(0.299, 0.450, 0.576, 1),
        'BackColor': Vec4(0.83, 1.02, 1.5, 1),
        'AmbientColor': Vec4(0.429, 0.66000, 0.920000, 1),
        'FogColor': Vec4(0.02, 0.0400, 0.149, 0),
        'FogExp': 0.0030000000260800002,
        'SkyType': SKY_NIGHT,
        'StarColor': Vec4(1, 1, 1, 0.25),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.149, 0.4, 0.450, 1),
        'SeaColorShader': Vec4(0.100, 0.200, 0.149, 1) },
    'Stars': {
        'Direction': Vec3(0, 40, 20),
        'FrontColor': Vec4(0.390, 0.489, 0.91000, 1),
        'BackColor': Vec4(0.78000, 1, 1.22, 1),
        'AmbientColor': Vec4(0.510, 0.576, 0.815, 1),
        'FogColor': Vec4(0, 0, 0, 0),
        'FogExp': 0.0010000000475,
        'SkyType': SKY_STARS,
        'StarColor': Vec4(1, 1, 1, 1),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.149, 0.348, 0.550000, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) },
    'Halloween': {
        'Direction': Vec3(0, 300, 70),
        'FrontColor': Vec4(0.299, 0.200, 0.53000, 1),
        'BackColor': Vec4(0.418, 0.63, 0.38, 1),
        'AmbientColor': Vec4(0.75, 0.815, 0.565, 1),
        'FogColor': Vec4(0.08, 0.050000, 0.11, 0),
        'FogExp': 0.0012000000570000001,
        'SkyType': SKY_HALLOWEEN,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) },
    'FullMoon': {
        'Direction': Vec3(0, 300, 110),
        'FrontColor': Vec4(0.299, 0.200, 0.53000, 1),
        'BackColor': Vec4(0.478, 1.06, 0.760, 1),
        'AmbientColor': Vec4(0.38, 0.65, 0.77, 1),
        'FogColor': Vec4(0.11, 0.08, 0.140, 0),
        'FogExp': 0.0,
        'SkyType': SKY_HALLOWEEN,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) },
    'HalfMoon': {
        'Direction': Vec3(0, 300, 110),
        'FrontColor': Vec4(0.299, 0.200, 0.53000, 1),
        'BackColor': Vec4(0.385826, 0.346457, 0.267716, 1),
        'AmbientColor': Vec4(0.66000, 0.685, 0.989, 1),
        'FogColor': Vec4(0.070, 0.050000, 0.089, 0),
        'FogExp': 0.000250,
        'SkyType': SKY_HALLOWEEN,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 0.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) },
    'HalfMoon2': {
        'Direction': Vec3(0, 300, 110),
        'FrontColor': Vec4(0.299, 0.200, 0.53000, 1),
        'BackColor': Vec4(0.565, 0.670000, 0.4, 1),
        'AmbientColor': Vec4(0.66000, 0.760, 0.408, 1),
        'FogColor': Vec4(0.08, 0.050000, 0.089, 0),
        'FogExp': 0.000250,
        'SkyType': SKY_HALLOWEEN,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 0.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) },
    'Invasion': {
        'Direction': Vec3(0, 300, 110),
        'FrontColor': Vec4(0.299, 0.239, 0.670000, 1),
        'BackColor': Vec4(0.739, 0.848, 0.52, 1),
        'AmbientColor': Vec4(0.66000, 0.760, 0.408, 1),
        'FogColor': Vec4(0.100, 0.12, 0.0299, 0),
        'FogExp': 0.000250,
        'SkyType': SKY_INVASION,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.5,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) } }
ENV_SETTINGS_OPENSKY = { }
ENV_SETTINGS_NO_HOLIDAY = { }
ENV_SETTINGS_FOREST = {
    'BASE': {
        'FrontColor': Vec4(1.87, 1.51, 1.25, 1),
        'BackColor': Vec4(0.34, 0.71, 0.418, 1),
        'AmbientColor': Vec4(0.62, 0.78000, 0.88, 1),
        'FogColor': Vec4(0.209, 0.28000, 0.22, 0),
        'FogExp': 0.0017999999690800001 },
    'Dawn': {
        'Direction': Vec3(0, 35, 210),
        'FrontColor': Vec4(1.51, 1.5, 1.01, 1),
        'BackColor': Vec4(0.288, 0.540000, 0.390, 1),
        'AmbientColor': Vec4(0.22, 0.348, 0.540000, 1),
        'FogColor': Vec4(0.27, 0.44, 0.450, 0),
        'FogExp': 0.00300,
        'SkyType': SKY_DAWN },
    'Day': {
        'FrontColor': Vec4(2, 1.79, 1.67, 1),
        'BackColor': Vec4(0.239, 0.489, 0.418, 1),
        'AmbientColor': Vec4(0.670000, 0.848, 0.91000, 1),
        'FogColor': Vec4(0.598, 0.696, 0.9, 0),
        'FogExp': 0.00060000002849800002 },
    'Dusk': {
        'Direction': Vec3(0, 35, 15),
        'FrontColor': Vec4(1.73, 1.04, 0.930000, 1),
        'BackColor': Vec4(0.489, 0.66000, 0.418, 1),
        'AmbientColor': Vec4(0.38, 0.299, 0.44, 1),
        'FogColor': Vec4(0.359, 0.288, 0.12, 0),
        'FogExp': 0.002,
        'SkyType': SKY_DUSK },
    'Night': {
        'Direction': Vec3(0, 40, 90),
        'FrontColor': Vec4(0.260, 0.609, 0.478, 1),
        'BackColor': Vec4(0.5, 0.920000, 1.41, 1),
        'AmbientColor': Vec4(0.37, 0.62, 0.680000, 1),
        'FogColor': Vec4(0, 0.070, 0.070, 0),
        'FogExp': 0.0020000000949899998,
        'SkyType': SKY_NIGHT },
    'Stars': {
        'Direction': Vec3(0, 40, 160),
        'FrontColor': Vec4(0.260, 0.489, 0.560000, 1),
        'BackColor': Vec4(0.946, 0.946, 1.14, 1),
        'AmbientColor': Vec4(0.25, 0.58, 0.58, 1),
        'FogColor': Vec4(0, 0, 0, 0),
        'FogExp': 0.00079999997979000002,
        'SkyType': SKY_NIGHT } }
ENV_SETTINGS_SWAMP = {
    'BASE': {
        'FrontColor': Vec4(1.7, 1.7, 1.39, 1),
        'BackColor': Vec4(0.598, 0.9, 1.5, 1),
        'AmbientColor': Vec4(0.9, 0.9, 0.800000, 1),
        'FogColor': Vec4(0.200, 0.25, 0.299, 0),
        'FogExp': 0.00500,
        'SkyType': SKY_SWAMP,
        'StarColor': Vec4(1, 1, 1, 0) },
    'Dawn': {
        'Direction': Vec3(0, 35, 210),
        'FrontColor': Vec4(1.79, 1.8, 1.25, 1),
        'BackColor': Vec4(0.418, 0.66000, 0.359, 1),
        'AmbientColor': Vec4(0.78000, 0.890, 0.890, 1),
        'FogColor': Vec4(0.13, 0.288, 0.299, 0),
        'FogExp': 0.008,
        'FogLinearRange': (0.0, 250.0),
        'SkyType': SKY_DUSK },
    'Day': {
        'FrontColor': Vec4(1.84, 1.85, 1.58, 1),
        'BackColor': Vec4(0.565, 0.890, 0.62, 1),
        'AmbientColor': Vec4(0.78000, 0.890, 0.920000, 1),
        'FogColor': Vec4(0.288, 0.348, 0.38, 0),
        'SkyType': SKY_DAY },
    'Dusk': {
        'Direction': Vec3(0, 35, 15),
        'FrontColor': Vec4(1.76, 1.39, 1.31, 1),
        'BackColor': Vec4(0.390, 0.53000, 0.75, 1),
        'AmbientColor': Vec4(0.848, 0.890, 0.800000, 1),
        'SkyType': SKY_DUSK },
    'Night': {
        'Direction': Vec3(0, 40, 90),
        'FrontColor': Vec4(0.418, 0.565, 0.540000, 1),
        'BackColor': Vec4(0.935, 1.15, 1.51, 1),
        'AmbientColor': Vec4(0.418, 0.706, 0.75, 1),
        'FogColor': Vec4(0.11, 0.13, 0.179, 0),
        'FogExp': 0.0049999998882400004,
        'SkyType': SKY_NIGHT },
    'Stars': {
        'Direction': Vec3(0, 40, 160),
        'FrontColor': Vec4(0.429, 0.5, 0.956, 1),
        'BackColor': Vec4(1.04, 1.23, 1.7, 1),
        'AmbientColor': Vec4(0.550000, 0.826, 0.848, 1),
        'FogColor': Vec4(0, 0, 0, 0),
        'FogExp': 0.0030000000260800002,
        'SkyType': SKY_STARS } }
ENV_SETTINGS_CAVE = {
    'BASE': {
        'Direction': Vec3(0, 0, 270),
        'LightSwitch': [
            0,
            1,
            0],
        'FrontColor': Vec4(0, 0, 0, 1),
        'BackColor': Vec4(0, 0, 0, 1),
        'AmbientColor': Vec4(0.25, 0.25, 0.25, 1),
        'FogType': FOG_LINEAR,
        'FogColor': Vec4(0.149, 0.149, 0.050000, 0),
        'FogExp': 0.002,
        'FogLinearRange': (0.0, 400.0),
        'SkyType': SKY_OFF,
        'StarColor': Vec4(1, 1, 1, 0) } }
ENV_SETTINGS_INTERIOR = {
    'BASE': {
        'Direction': Vec3(0, 0, 270),
        'LightSwitch': [
            0,
            0,
            0],
        'FrontColor': Vec4(0, 0, 0, 1),
        'BackColor': Vec4(0, 0, 0, 1),
        'AmbientColor': Vec4(1, 0.25, 0.25, 1),
        'FogType': FOG_OFF,
        'FogColor': Vec4(0.25, 0.25, 0.25, 0),
        'FogExp': 0.0001,
        'FogLinearRange': (0.0, 100.0),
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.200, 0.200, 0.200, 1),
        'SeaColorShader': Vec4(0.200, 0.200, 0.200, 1) } }
ENV_SETTINGS_SAILING = {
    'Dawn': {
        'FogColor': Vec4(0.288, 0.320, 0.44, 0),
        'FogExp': 0.0015 },
    'Day': {
        'FogColor': Vec4(0.598, 0.696, 0.9, 0),
        'FogExp': 0.000898 },
    'Dusk': {
        'FogExp': 0.000500 },
    'Night': {
        'FrontColor': Vec4(0.299, 0.450, 0.576, 1),
        'BackColor': Vec4(1.33, 1.5, 1.62, 1),
        'AmbientColor': Vec4(0.19, 0.510, 0.87, 1),
        'FogColor': Vec4(0.11, 0.179, 0.33, 0),
        'FogExp': 0.001 },
    'Stars': {
        'FrontColor': Vec4(0.390, 0.489, 0.91000, 1),
        'BackColor': Vec4(1.28, 1.38, 1.52, 1),
        'AmbientColor': Vec4(0.418, 0.510, 0.790000, 1),
        'FogColor': Vec4(0.089, 0.089, 0.239, 0),
        'FogExp': 0.001 } }
ENV_SETTINGS_CLOUDY = {
    'BASE': {
        'FrontColor': Vec4(1.7, 1.7, 1.39, 1),
        'BackColor': Vec4(0.598, 0.9, 1.5, 1),
        'AmbientColor': Vec4(0.9, 0.9, 0.800000, 1),
        'FogColor': Vec4(0.200, 0.25, 0.299, 0),
        'FogExp': 0.00500,
        'SkyType': SKY_SWAMP,
        'StarColor': Vec4(1, 1, 1, 0) } }
ENV_SETTINGS_INVASION = {
    'BASE': {
        'Direction': Vec3(0, 300, 110),
        'FrontColor': Vec4(0.299, 0.239, 0.670000, 1),
        'BackColor': Vec4(0.739, 0.848, 0.52, 1),
        'AmbientColor': Vec4(0.66000, 0.760, 0.408, 1),
        'FogColor': Vec4(0.100, 0.12, 0.0299, 0),
        'FogExp': 0.000250,
        'SkyType': SKY_INVASION,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.5,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) } }
ENV_SETTINGS_SAINT_PATRICKS = {
    'BASE': {
        'SeaColor': Vec4(0.25, 0.9, 0.200, 1.0),
        'SeaColorShader': Vec4(0.22, 0.560000, 0.149, 1),
        'SeaFactor': Vec3(0.4, 1.0, 0.299) } }
ENV_SETTINGS_VALENTINES = {
    'Day': {
        'FrontColor': Vec4(1.71, 1.36, 1.14, 1),
        'BackColor': Vec4(0.58, 0.58, 0.88, 1),
        'AmbientColor': Vec4(0.52, 0.390, 0.418, 1),
        'FogColor': Vec4(0.46, 0.38, 0.429, 0),
        'FogExp': 0.00060000002849800002,
        'SkyType': SKY_DUSK,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.348, 0.5, 0.62, 1),
        'SeaColorShader': Vec4(0.25, 0.25, 0.149, 1) } }
ENV_SETTINGS_HALLOWEEN = {
    'Dusk': {
        'FrontColor': Vec4(1.7, 1.7, 1.39, 1),
        'BackColor': Vec4(0.598, 0.9, 1.5, 1),
        'AmbientColor': Vec4(0.9, 0.9, 0.800000, 1),
        'FogColor': Vec4(0.200, 0.25, 0.299, 0),
        'FogExp': 0.00500,
        'SkyType': SKY_OVERCAST,
        'StarColor': Vec4(1, 1, 1, 0) },
    'Night': {
        'FrontColor': Vec4(0.299, 0.200, 0.53000, 1),
        'BackColor': Vec4(0.418, 0.63, 0.38, 1),
        'AmbientColor': Vec4(0.75, 0.815, 0.565, 1),
        'FogColor': Vec4(0.08, 0.050000, 0.11, 0),
        'FogExp': 0.0012000000570000001,
        'SkyType': SKY_HALLOWEEN,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) },
    'Stars': {
        'FrontColor': Vec4(0.299, 0.200, 0.53000, 1),
        'BackColor': Vec4(0.418, 0.63, 0.38, 1),
        'AmbientColor': Vec4(0.75, 0.815, 0.565, 1),
        'FogColor': Vec4(0.08, 0.050000, 0.11, 0),
        'FogExp': 0.0012000000570000001,
        'SkyType': SKY_HALLOWEEN,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) } }
ENV_SETTINGS_CURSED_NIGHT = {
    'Dawn': {
        'MoonPhase': 0.0 },
    'Dusk': {
        'Direction': Vec3(0, 65, 90),
        'SkyType': SKY_HALLOWEEN,
        'FogColor': Vec4(0.08, 0.050000, 0.11, 0),
        'MoonPhase': 0.0,
        'MoonSize': 1.39 },
    'Night': {
        'Direction': Vec3(0, 65, 90),
        'FrontColor': Vec4(0.299, 0.200, 0.53000, 1),
        'BackColor': Vec4(0.418, 0.63, 0.38, 1),
        'AmbientColor': Vec4(0.75, 0.815, 0.565, 1),
        'FogColor': Vec4(0.08, 0.050000, 0.11, 0),
        'FogExp': 0.0012000000570000001,
        'SkyType': SKY_HALLOWEEN,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.8,
        'MoonOverlay': 0.0,
        'MoonPhase': 0.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) },
    'Stars': {
        'Direction': Vec3(0, 65, 90),
        'FrontColor': Vec4(0.299, 0.200, 0.53000, 1),
        'BackColor': Vec4(0.418, 0.63, 0.38, 1),
        'AmbientColor': Vec4(0.75, 0.815, 0.565, 1),
        'FogColor': Vec4(0.08, 0.050000, 0.11, 0),
        'FogExp': 0.0012000000570000001,
        'SkyType': SKY_HALLOWEEN,
        'StarColor': Vec4(1, 1, 1, 0),
        'MoonSize': 1.8,
        'MoonOverlay': 0.0,
        'MoonPhase': 0.0,
        'SeaColor': Vec4(0.4, 0.598, 0.598, 1),
        'SeaColorShader': Vec4(0.100, 0.149, 0.100, 1) } }
ENV_SETTINGS_EVER_NIGHT = {
    'BASE': {
        'Direction': Vec3(0, 40, 90),
        'FrontColor': Vec4(0.299, 0.450, 0.576, 1),
        'BackColor': Vec4(0.83, 1.02, 1.5, 1),
        'AmbientColor': Vec4(0.429, 0.66000, 0.920000, 1),
        'FogColor': Vec4(0.02, 0.0400, 0.149, 0),
        'FogExp': 0.0030000000260800002,
        'SkyType': SKY_NIGHT,
        'StarColor': Vec4(1, 1, 1, 0.25),
        'MoonSize': 1.0,
        'MoonOverlay': 0.0,
        'MoonPhase': 1.0,
        'SeaColor': Vec4(0.149, 0.4, 0.450, 1),
        'SeaColorShader': Vec4(0.100, 0.200, 0.149, 1) } }
ENV_SETTINGS_CANNONGAME = {
    'Dawn': {
        'FogExp': 0.000898,
        'Direction': Vec3(0, 30, 245),
        'LightSwitch': [
            1,
            1,
            1] },
    'Night': {
        'FogExp': 9.e-005,
        'Direction': Vec3(0, 30, 245),
        'LightSwitch': [
            1,
            1,
            1] },
    'Stars': {
        'FogExp': 9.e-005,
        'Direction': Vec3(0, 30, 245),
        'LightSwitch': [
            1,
            1,
            1] } }
