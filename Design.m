%% Design antenna and steering radiation pattern
% Specify resonant frequency and radiation wave speed
fc = 2.4e9; %2.4Ghz
c = physconst('lightspeed');
lambda = c/fc;

% patchMicrostrip element
patchElement = design(patchMicrostrip, fc); % create patchMicrostrip to resonate at 2.4Ghz
patchElement.Tilt = 90; % rotate the patch antenna so by 90 degrees so the radiation pattern occur along the x-axis
patchElement.TiltAxis = [0 1 0];

% Uniform rectangular antenna array
a = phased.URA;
a.Size = [2 5];
a.ElementSpacing = [0.5*lambda 0.5*lambda];
a.Element = patchElement;

% Create a steering vector
hsv = phased.SteeringVector('SensorArray', a);

% Specify steer direction in given degree azimuth and 0 degree evalation
azel = [-60; 0];
sv = step(hsv,fc,azel);

% 3-D radiation pattern of the antenna array
% pattern(a,fc);

% Plot array response before steering and after steering
subplot(211);
plotResponse(a,fc,c,'RespCut','Az','Format','Polar');
subplot(212)
plotResponse(a,fc,c,'RespCut','Az','Weights',sv,'Format','Polar');
