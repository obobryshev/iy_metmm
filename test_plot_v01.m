% 
% Files needed this script to work:
% 
% 2021-07-25   Created by Alex Bobryshev
% 
%% ------------------------------------------------------------------------- %%
%                                                                             %
%                           START. MAIN VARIABLES
%                                                                             %
%% ------------------------------------------------------------------------- %%
%

clear; close all; clc

str.comp = computer;
str.comp=lower(str.comp);

if strcmp(str.comp,'glnxa64')==1
    str.main_folder='/scratch/uni/u237/users/obobryshev/';
end
 
str.main_folder = fullfile(str.main_folder, 'oxygen_study/110_iyaux_Garand/');
str.results_path = fullfile(str.main_folder, 'iy_metmm/Output/'); 

str.model='TRE05';
%%
disp('1');
if strcmp(str.model, 'TRE05')
    %str.fname = '2021-07-19_2200'; %'2021-07-25_0547';
    %str.fname = '2021-07-25_0547';
%     str.fname = '2021-07-25_1627'; % "O2,O2-PWR98",
%     str.fname = '2021-07-25_1631'; % "H2O", "O2,O2-PWR98",
%     str.fname = '2021-07-25_1643'; % "H2O", "O2-MPM93, O2-SelfContMPM93",
%     str.fname = '2021-07-25_1728'; % MPM-2020
%     str.fname = '2021-07-25_1807'; % "AER"
%     str.fname_fgr = fullfile(str.results_path, [str.fname, '_fgrid.xml']);
%     str.fname_tmp = fullfile(str.results_path, [str.fname, '_out.0.xml']);
    % iy_O2-MPM2020_midlat-s_2021-07-30_0744.xml
    str.fname = '2021-08-28_0016';
    str.fname_fgr = fullfile(str.results_path, ['fgrid_O2-TRE05_', str.fname, '.xml']);
    str.fname_tmp = fullfile(str.results_path, ['iy_O2-TRE05_midlat-s_', str.fname, '.xml'])
elseif strcmp(str.model, 'MPM2020')
    % fgrid_O2-MPM20202021-07-29_2340.xml 
    % fgrid_O2-MPM2020_2021-08-06_0715.xml
    str.fname = '2021-08-28_0012';
    str.fname_fgr = fullfile(str.results_path, ['fgrid_O2-MPM2020_', str.fname, '.xml']);
    str.fname_tmp = fullfile(str.results_path, ['iy_O2-MPM2020_midlat-s_', str.fname, '.xml'])
elseif strcmp(str.model, 'AER')
    str.fname_fgr = fullfile(str.results_path, '' );
    str.fname_tmp = fullfile(str.results_path, '');
    return
else
    return
end


%%
fgrid = xmlLoad(str.fname_fgr);
tb = xmlLoad(str.fname_tmp);

%%

close all
plot(fgrid/1e9,tb)
xlabel('Frequency, GHz')
ylabel('T_B, iy')
ax=gca;
ax.FontSize = 14;
%%

str.savepath_final = fullfile(str.results_path, ['Plot_O2-MPM2020_', str.fname]);
%setenv( 'CONV_PDF', str.savepath_final);
print('-r300', '-dpng', str.savepath_final );
%!convert $CONV_PDF.png -trim +repage $CONV_PDF-crop.png
%!eog $CONV_PDF-crop.png
%!open $CONV_PDF-crop.png