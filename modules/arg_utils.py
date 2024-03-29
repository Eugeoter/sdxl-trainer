import argparse
import json


def add_model_arguments(parser: argparse.ArgumentParser):
    # Model Parameters
    parser.add_argument("--pretrained_model_name_or_path", type=str, default=None, help="Pretrained model name or path / 预训练模型名称或路径")
    parser.add_argument("--vae", type=str, default=None, help="VAE model path / VAE 模型路径")
    parser.add_argument("--no_half_vae", action='store_true', help="Do not use half VAE / 不使用半精度 VAE")
    parser.add_argument("--tokenizer_cache_dir", type=str, default=None, help="Tokenizer cache directory / 分词器缓存目录")
    parser.add_argument("--max_token_length", type=int, default=225, help="Maximum token length / 最大词元长度")
    parser.add_argument("--output_dir", type=str, default='outputs', help="Output directory / 输出目录")
    parser.add_argument("--mem_eff_attn", action='store_true', help="Use memory efficient attention / 使用内存高效的注意力机制，不能和 xformers 同时使用")
    parser.add_argument("--xformers", action='store_true', help="Use xformers / 使用 xformers ，不能和 mem_eff_attn 同时使用")
    parser.add_argument("--diffusers_xformers", action='store_true', help="Use diffusers xformers / 使用 diffusers xformers")
    parser.add_argument("--sdpa", action='store_true', help="Use SDPA / 使用 SDPA")
    parser.add_argument("--clip_skip", type=int, default=1, help="CLIP skip value / CLIP 跳过值")


def add_eval_arguments(parser: argparse.ArgumentParser):
    # Evaluation Parameters
    parser.add_argument("--benchmark_file", type=str, default=None, help="Benchmark file / 基准文件")
    parser.add_argument("--num_samples_per_prompt", type=int, default=1, help="Number of samples per prompt / 每个提示的样本数")
    parser.add_argument("--batch_size", type=int, default=1, help="Batch size / 批次大小")
    parser.add_argument("--cpu", action='store_true', help="Use CPU for inference / 使用 CPU 推理")
    parser.add_argument("--mixed_precision", type=str, default='fp16', help="Mixed precision type / 混合精度类型")
    parser.add_argument("--full_bf16", action='store_true', help="Use full BF16 precision / 使用全BF16精度训练")
    parser.add_argument("--full_fp16", action='store_true', help="Use full FP16 precision / 使用全FP16精度训练")
    parser.add_argument("--sample_sampler", type=str, default="ddim",
                        choices=["ddim", "pndm", "lms", "euler", "euler_a", "heun", "dpm_2", "dpm_2_a", "dpmsolver",
                                 "dpmsolver++", "dpmsingle", "k_lms", "k_euler", "k_euler_a", "k_dpm_2", "k_dpm_2_a"],
                        help=f"sampler (scheduler) type for sample images / 用于生成样本图像的采样器（调度器）类型")


def add_train_arguments(parser: argparse.ArgumentParser):
    # Training Parameters
    parser.add_argument("--num_train_epochs", type=int, default=100, help="Number of training epochs / 总训练期数")
    parser.add_argument("--batch_size", type=int, default=1, help="Batch size / 批次大小")
    parser.add_argument("--learning_rate", type=float, default=1e-6, help="Learning rate / 学习率")
    parser.add_argument("--block_lr", type=str, default=None, help="Block learning rate / 块学习率")
    parser.add_argument("--lr_scheduler", type=str, default='cosine', help="LR scheduler type / 学习率调度器类型")
    parser.add_argument("--lr_warmup_steps", type=int, default=0, help="LR warmup steps / 学习率预热步数")
    parser.add_argument("--lr_scheduler_power", type=float, default=1.0, help="LR scheduler power / 多项式调度器的幂")
    parser.add_argument("--lr_scheduler_num_cycles", type=int, default=1, help="Number of LR scheduler cycles / 带重启余弦调度器的重启周期数")
    parser.add_argument("--lr_scheduler_args", nargs='+', default=[], help="Additional LR scheduler arguments / 学习率调度器附加参数")
    parser.add_argument("--mixed_precision", type=str, default='fp16', help="Mixed precision type / 混合精度类型")
    parser.add_argument("--full_bf16", action='store_true', help="Use full BF16 precision / 使用全BF16精度训练")
    parser.add_argument("--full_fp16", action='store_true', help="Use full FP16 precision / 使用全FP16精度训练")
    parser.add_argument("--train_text_encoder", action='store_true', help="Train text encoder / 训练文本编码器")
    parser.add_argument("--learning_rate_te1", type=float, default=None, help="Learning rate for text encoder 1 / 文本编码器1 (CLIP L) 的学习率")
    parser.add_argument("--learning_rate_te2", type=float, default=None, help="Learning rate for text encoder 2 / 文本编码器2 (CLIP G) 的学习率")

    parser.add_argument("--gradient_checkpointing", action='store_true', help="Use gradient checkpointing / 使用梯度检查点")
    parser.add_argument("--gradient_accumulation_steps", type=int, default=1, help="Gradient accumulation steps / 梯度累积步数")
    parser.add_argument("--optimizer_type", type=str, default='AdamW8Bit', help="Optimizer type / 优化器类型")
    parser.add_argument("--optimizer_args", type=str, default='*', help="Additional optimizer arguments / 优化器附加参数")
    parser.add_argument("--noise_offset", type=float, default=0.0, help="Noise offset value / 噪声偏移值")
    parser.add_argument("--multires_noise_iterations", type=int, default=0, help="Multi-resolution noise iterations / 多分辨率噪声迭代次数")
    parser.add_argument("--multires_noise_discount", type=float, default=0.25, help="Multi-resolution noise discount / 多分辨率噪声折扣")
    parser.add_argument("--adaptive_noise_scale", type=float, default=None, help="Adaptive noise scale / 自适应噪声规模")
    parser.add_argument("--max_grad_norm", type=float, default=0.0, help="Maximum gradient norm / 最大梯度范数")
    parser.add_argument("--zero_terminal_snr", action='store_true', help="Use zero terminal SNR / 使用零终端信噪比")
    parser.add_argument("--ip_noise_gamma", type=float, default=0.0, help="IP noise gamma / 扰动噪声伽马")
    parser.add_argument("--min_snr_gamma", type=float, default=5.0, help="Minimum SNR gamma / 最小信噪比伽马")
    parser.add_argument("--scale_v_pred_loss_like_noise_pred", action='store_true', help="Scale V prediction loss like noise prediction / 缩放 V 预测损失，如噪声预测")
    parser.add_argument("--v_pred_like_loss", type=float, default=0.0, help="V prediction like loss / V 预测损失")
    parser.add_argument("--debiased_estimation_loss", action='store_true', help="Use debiased estimation loss / 使用去偏估计损失")
    parser.add_argument("--min_timestep", type=int, default=0, help="Minimum timestep / 最小时间步长")
    parser.add_argument("--max_timestep", type=int, default=1000, help="Maximum timestep / 最大时间步长")
    parser.add_argument("--cpu", action='store_true', help="Use CPU for training / 使用 CPU 训练")

    # Dataset Parameters
    parser.add_argument("--image_dir", type=str, default=None, help="Directory of images / 图像目录")
    parser.add_argument("--metadata_file", type=str, default=None, help="Path to metadata file / 数据集的元数据文件路径，记录了所有数据的标注信息")
    parser.add_argument("--recording_dir", type=str, default=None, help="Directory of records / 记录目录，存放第一次数据集加载的结果，避免二次加载时做重复计算")
    parser.add_argument("--flip_aug", action='store_true', help="Use flip augmentation / 使用随机水平翻转的数据增强")
    parser.add_argument("--bucket_reso_step", type=int, default=32, help="Bucket resolution step / 分桶步长")
    parser.add_argument("--tags_shuffle_prob", type=float, default=0.0, help="Shuffle captions probability / 混洗标注概率")
    parser.add_argument("--tags_shuffle_rate", type=float, default=1.0, help="Shuffle captions rate / 混洗标注率")
    parser.add_argument("--fixed_tag_dropout_rate", type=float, default=0.0, help="Caption fixed tag dropout rate / 标注的固定标签丢弃率")
    parser.add_argument("--flex_tag_dropout_rate", type=float, default=0.0, help="Caption flex tag dropout rate / 标注的灵活标签丢弃率")
    parser.add_argument("--resolution", type=int, default=1024, help="Resolution / 分辨率")
    parser.add_argument("--vae_batch_size", type=int, default=1, help="VAE batch size / VAE 批次大小")
    parser.add_argument("--max_dataset_n_workers", type=int, default=4, help="Maximum number of dataset workers / 最大数据集工作进程数")
    parser.add_argument("--max_dataloader_n_workers", type=int, default=4, help="Maximum number of data loader workers / 最大数据加载器工作进程数")
    parser.add_argument("--persistent_data_loader_workers", action='store_true', help="Use persistent data loader workers / 使用持久化数据加载器工作进程")

    # parser.add_argument("--use_safetensors", action='store_true', help="Use safetensors / 使用 safetensors 格式")

    # OS Parameters
    parser.add_argument("--output_dir", type=str, default='outputs', help="Output directory / 输出目录")
    parser.add_argument("--output_name", type=str, default='model', help="Output model name / 输出模型的名称")
    parser.add_argument("--logging_dir", type=str, default='logging', help="Logging directory / 日志目录")
    parser.add_argument("--loss_recorder_gamma", type=float, default=0.9, help="Loss recorder gamma / 损失记录器伽马")
    parser.add_argument("--loss_recorder_stride", type=int, default=1000, help="Loss record stride / 损失记录步幅，即多少步损失平均一次")
    parser.add_argument("--save_precision", type=str, default='float', help="Save precision / 保存精度")
    parser.add_argument("--save_every_n_epochs", type=int, default=None, help="Save every N epochs / 每 N 个周期保存一次")
    parser.add_argument("--save_every_n_steps", type=int, default=None, help="Save every N steps / 每 N 个步骤保存一次")
    parser.add_argument("--save_on_train_end", action='store_true', help="Save on training end / 训练结束时保存")
    parser.add_argument("--save_on_keyboard_interrupt", action='store_true', help="Save on keyboard interrupt / 键盘中断时保存")
    parser.add_argument("--save_on_exception", action='store_true', help="Save on exception / 异常时保存")
    parser.add_argument("--sample_every_n_epochs", type=int, default=None, help="Sample every N epochs / 每 N 个周期采样一次")
    parser.add_argument("--sample_every_n_steps", type=int, default=None, help="Sample every N steps / 每 N 个步骤采样一次")
    parser.add_argument("--sample_prompts", type=str, default=None, help="file for prompts to generate sample images / 用于生成样本图像的提示文件")
    parser.add_argument("--sample_sampler", type=str, default="ddim",
                        choices=["ddim", "pndm", "lms", "euler", "euler_a", "heun", "dpm_2", "dpm_2_a", "dpmsolver",
                                 "dpmsolver++", "dpmsingle", "k_lms", "k_euler", "k_euler_a", "k_dpm_2", "k_dpm_2_a"],
                        help=f"sampler (scheduler) type for sample images / 用于生成样本图像的采样器（调度器）类型")

    # Cache Parameters
    parser.add_argument("--cache_latents", action='store_true', help="Cache latents / 缓存潜变量")
    parser.add_argument("--cache_latents_to_disk", action='store_true', help="Cache latents to disk / 缓存潜变量到磁盘")
    parser.add_argument("--check_cache_validity", action='store_true', help="Check cache validity / 在训练前检查缓存有效性")
    parser.add_argument("--keep_cached_latents_in_memory", action='store_true', help="Keep latents in memory / 在内存中保留加载的潜变量")
    parser.add_argument("--async_cache", action='store_true', help="Use async cache / 使用异步缓存")

    parser.add_argument("--control", action='store_true', help="Use control / 使用控制")
